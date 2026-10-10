"""从热搜 CSV 按标题出现次数或词频生成中文词云。"""

import argparse
import csv
import os
import re
from collections import Counter
from pathlib import Path

import jieba
from wordcloud import WordCloud


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_KEEP_WORDS = {"美", "英", "法", "俄", "伊", "12306"}


def load_stopwords(path):
    """每行一个词，忽略空行和以 # 开头的注释。"""
    return {
        line.strip().casefold()
        for line in path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def build_frequencies(input_path, tokenizer, stopwords, keep_words,
                      month=None, count_mode="titles"):
    frequencies = Counter()
    accepted = skipped = 0
    keep_words = {word.casefold() for word in keep_words}
    with input_path.open(encoding="utf-8-sig", newline="") as file:
        for row in csv.reader(file):
            if row[:2] == ["时间", "热搜"]:
                continue
            if len(row) < 2 or not row[1].strip():
                skipped += 1
                continue
            if month and row[0].strip()[:7] != month:
                continue
            accepted += 1
            words = []
            for token in tokenizer.lcut(row[1]):
                word = token.strip()
                if not word:
                    continue
                if word.casefold() in keep_words:
                    words.append(word)
                elif (word.casefold() not in stopwords and len(word) > 1
                      and any(char.isalpha() for char in word)):
                    words.append(word)
            # 标题内去重，但保留跨标题、跨日期重复上榜的次数。
            frequencies.update(dict.fromkeys(words).keys() if count_mode == "titles" else words)
    return frequencies, accepted, skipped


def find_font(requested=None):
    if requested:
        path = Path(requested).expanduser()
        if not path.is_file():
            raise ValueError(f"字体文件不存在：{path}")
        return str(path)
    candidates = [
        Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts/msyh.ttc",
        Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts/simhei.ttf",
        Path("/usr/share/fonts/Chinese/simhei.ttf"),
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
        Path("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"),
        Path("/System/Library/Fonts/PingFang.ttc"),
    ]
    for path in candidates:
        if path.is_file():
            return str(path)
    raise ValueError("未找到中文字体，请通过 --font 指定中文 .ttf 或 .ttc 文件。")


def parse_month(value):
    if not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", value) or value.startswith("0000"):
        raise argparse.ArgumentTypeError("月份格式应为 YYYY-MM，例如 2025-07。")
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=BASE_DIR / "Archieved_jul.csv",
                        help="输入 CSV，前两列为时间、热搜；默认使用七月归档")
    parser.add_argument("--output", type=Path, help="输出 PNG；默认保存至项目 assets 目录")
    parser.add_argument("--month", type=parse_month, help="仅统计指定月份，例如 2025-07")
    parser.add_argument("--stopwords", type=Path, default=BASE_DIR / "stopwords.txt")
    parser.add_argument("--userdict", type=Path, default=BASE_DIR / "userdict.txt")
    parser.add_argument("--font", help="中文字体路径；默认自动查找")
    parser.add_argument("--count-mode", choices=("titles", "occurrences"), default="titles",
                        help="titles：每条标题内每词计一次；occurrences：统计全部词频")
    parser.add_argument("--keep-word", action="append", default=[],
                        help="额外保留的词，可重复指定；优先于停用词和长度过滤")
    args = parser.parse_args()

    try:
        stopwords = load_stopwords(args.stopwords)
        tokenizer = jieba.Tokenizer()
        tokenizer.load_userdict(str(args.userdict))
        for word in args.keep_word:
            tokenizer.add_word(word, freq=100000)
        frequencies, accepted, skipped = build_frequencies(
            args.input, tokenizer, stopwords, DEFAULT_KEEP_WORDS | set(args.keep_word),
            args.month, args.count_mode,
        )
        if not frequencies:
            raise ValueError("没有可用于词云的词，请检查输入、月份及过滤规则。")
        font_path = find_font(args.font)
        name = args.month or args.input.stem.removeprefix("Archieved_")
        output = args.output or BASE_DIR / "assets" / f"{name}.png"
        cloud = WordCloud(font_path=font_path, height=800, width=1000,
                          collocations=False, random_state=42)
        cloud.generate_from_frequencies(frequencies)
        output.parent.mkdir(parents=True, exist_ok=True)
        cloud.to_file(str(output))
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(1, f"生成失败：{error}\n")

    print(f"已读取 {accepted} 条热搜，跳过 {skipped} 条无效记录，保留 {len(frequencies)} 个词。")
    print("高频词：" + "、".join(f"{word}({count})" for word, count in frequencies.most_common(20)))
    print(f"词云已保存：{output.resolve()}")


if __name__ == "__main__":
    main()

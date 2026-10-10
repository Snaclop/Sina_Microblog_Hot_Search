# Sina Microblog Hot Search Spiders 微博热搜爬虫

利用新浪微博的开放接口`https://api.xhus.cn/api/rweibo?encode=json`获取数据

所有数据均保存在同目录下的`Hot_search.csv`文件里，并带有数据获取时间  
注：从2025年3月22日开始，将采用GitHub Actions实现爬虫的自动化获取数据，设定时间是北京时间20:00（UTC时间12:00）由于GitHub获得的时间是UTC时间，因此在`Hot_search.csv`文件里显示的时间是UTC时间而不是北京时间

## GitHub Actions 自动抓取

工作流位于 `.github/workflows/main.yml`，每天北京时间 20:00 抓取热搜，并仅提交 `Hot_search.csv`。支持手动运行，Python 版本固定为 3.12。定时任务可能有排队延迟。

工作流使用 GitHub 自动提供的 `GITHUB_TOKEN`，并在 YAML 中声明 `contents: write`，不再需要创建或续期 `PUSH_TOKEN`。原有 Secret 可以留着，当前工作流不会使用它。

启用和验证步骤：

1. 确保新版工作流已提交到仓库默认分支 `main`。
2. 打开仓库的 **Actions → Data Scraping**；若显示已停用，点击 **Enable workflow**。
3. 点击 **Run workflow**，选择 `main` 并运行一次。
4. 等待运行成功，确认仓库出现或更新 `Hot_search.csv`，以及机器人提交 `Update hot-search data`。

若提交步骤提示 403 或写权限不足，检查 **Settings → Actions → General → Workflow permissions**，选择 **Read and write permissions** 并保存。若组织策略或分支保护禁止直接提交，需要调整对应规则；`contents: write` 不会绕过分支保护。这里仅做数据抓取，不会自动生成词云。

官方说明：[工作流令牌权限](https://docs.github.com/en/actions/how-tos/security-for-github-actions/security-guides/automatic-token-authentication)、[手动运行](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow)、[重新启用](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows)。

已生成的月度词云：

2月热搜
![feb_png](./assets/feb.png)

4月热搜
![apr_png](./assets/apr.png)

5月热搜
![may_png](./assets/may.png)

6月热搜
![jun_png](./assets/jun.png)

7月热搜
![jul_png](./assets/jul.png)

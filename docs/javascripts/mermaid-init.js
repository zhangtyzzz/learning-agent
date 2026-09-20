// Material 主题下初始化 mermaid（配合 superfences 的 custom fence）
document$.subscribe(() => {
  mermaid.initialize({
    startOnLoad: true,
    theme: document.body.getAttribute("data-md-color-scheme") === "slate" ? "dark" : "default",
  });
  mermaid.run();
});

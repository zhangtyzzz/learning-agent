const remarkMath = require("remark-math").default;
const rehypeKatex = require("rehype-katex").default;
const remarkGithubBlockquoteAlert =
  require("remark-github-blockquote-alert").default;

const config = {
  title: "Agent 算法学习库",
  tagline: "后训练与 Agentic RL · 40 讲图文课程",
  favicon: "favicon.ico",
  url: "https://zhangtyzzz.github.io",
  baseUrl: "/learning-agent/",
  organizationName: "zhangtyzzz",
  projectName: "learning-agent",
  trailingSlash: false,
  onBrokenLinks: "warn",
  i18n: { defaultLocale: "zh-Hans", locales: ["zh-Hans"] },
  markdown: {
    mermaid: true,
    format: "md",
    hooks: { onBrokenMarkdownLinks: "warn" },
  },
  themes: [
    "@docusaurus/theme-mermaid",
    [
      "@easyops-cn/docusaurus-search-local",
      {
        hashed: false,
        language: ["zh", "en"],
        indexDocs: true,
        indexBlog: false,
        indexPages: false,
      },
    ],
  ],
  presets: [
    [
      "classic",
      {
        docs: {
          routeBasePath: "/",
      numberPrefixParser: false,
          sidebarPath: require.resolve("./sidebars.js"),
      remarkPlugins: [remarkMath, remarkGithubBlockquoteAlert],
      rehypePlugins: [rehypeKatex],
          
          
          editUrl: ({ docPath }) =>
            `https://github.com/zhangtyzzz/learning-agent/edit/master/docs/${docPath}`,
        },
        blog: false,
        theme: { customCss: require.resolve("./src/css/custom.css") },
      },
    ],
  ],
  themeConfig: {
    colorMode: { defaultMode: "light" },
    navbar: {
      title: "Agent 算法学习库",
      items: [
        { type: "doc", docId: "index", label: "首页", position: "left" },
        { to: "/ROADMAP", label: "学习路径", position: "left" },
        { to: "/wiki/workflow", label: "知识库", position: "left" },
        {
          href: "https://github.com/zhangtyzzz/learning-agent",
          position: "right",
          className: "header-github-link",
          "aria-label": "GitHub 仓库",
        },
      ],
    },
    footer: {
      style: "dark",
      copyright: `个人学习库 · Docusaurus 构建 · push 即自动更新`,
    },
    mermaid: { theme: { light: "default", dark: "dark" } },
  },
  headTags: [
    {
      tagName: "link",
      attributes: {
        rel: "stylesheet",
        href: "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css",
      },
    },
  ],
};

module.exports = config;

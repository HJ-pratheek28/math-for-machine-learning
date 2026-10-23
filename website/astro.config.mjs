import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

export default defineConfig({
  site: "https://hj-pratheek28.github.io",
  base: "/math-for-machine-learning",
  integrations: [starlight({
    title: "Math for ML Research Lab",
    description: "Derive it. Implement it. Test it. Connect it to ML.",
    social: { github: "https://github.com/HJ-pratheek28/math-for-machine-learning" },
    sidebar: [
      { label: "Start Here", items: [{ label: "Overview", link: "/" }] },
      { label: "Curriculum", items: [
        { label: "Roadmap", link: "/curriculum/roadmap" },
        { label: "Resource Map", link: "/curriculum/resource-map" }
      ] }
    ]
  })]
});

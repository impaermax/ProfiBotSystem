import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import Modules from "../components/Modules.vue";
import SiteAnalysis from "../components/SiteAnalysis.vue";
import TelegramBots from "../components/TelegramBots.vue";
import VoiceBots from "../components/VoiceBots.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/modules", component: Modules },
  { path: "/site-analysis", component: SiteAnalysis },
  { path: "/telegram-bots", component: TelegramBots },
  { path: "/voice-bots", component: VoiceBots },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

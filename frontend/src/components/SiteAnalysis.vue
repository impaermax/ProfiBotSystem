<template>
  <div>
    <h2>Анализ сайта</h2>
    <input v-model="url" placeholder="Введите URL" />
    <button @click="analyze">Анализировать</button>
    <pre>{{ result }}</pre>
  </div>
</template>

<script>
export default {
  data() {
    return {
      url: "",
      result: {},
    };
  },
  methods: {
    async analyze() {
      const response = await fetch("/api/site-analysis", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: this.url }),
      });
      this.result = await response.json();
    },
  },
};
</script>

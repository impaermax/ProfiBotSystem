<template>
  <div class="modules">
    <h2>Выберите раздел</h2>
    <button @click="$router.push('/site-analysis')">Анализ сайта</button>
    <button @click="$router.push('/telegram-bots')">Телеграм боты</button>
    <button @click="$router.push('/voice-bots')">Голосовые боты</button>
  </div>
</template>

<style scoped>
.modules {
  text-align: center;
  margin-top: 50px;
}

button {
  background-color: #6a0dad;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  margin: 10px;
  cursor: pointer;
}

button:hover {
  background-color: #510099;
}
</style>

<template>
  <div class="home">
    <h1>Приветствуем на нашей многофункциональной платформе Профи Бот Систем</h1>
    <button @click="$router.push('/modules')">Начать</button>
  </div>
</template>

<style scoped>
.home {
  text-align: center;
  margin-top: 50px;
}

button {
  background-color: #6a0dad;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #510099;
}
</style>

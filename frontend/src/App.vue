<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>
      |
      <router-link to="/chat">Live-Chat</router-link>
      |
      <router-link to="/register">Register</router-link>
      |
      <router-link to="/profile">Profile</router-link>
    </div>
  <router-view />
  </div>
</template>

<style lang="scss">
body {
  min-height: 100vh;
  overflow:visible;
  background: linear-gradient(180deg, #22c1c3, #fdbb2d);
  margin-bottom: 11vh;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #316870;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #000000;
    font-size: 30px;

    &.router-link-exact-active {
      color: #FFFFFF;
    }
  }
}
</style>

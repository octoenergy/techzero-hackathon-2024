<template>
  <header class="header">
    <div class="content-container">
      <h1>GreenCloud Server Energy Reporting</h1>
    </div>
    <div class="logo-container">
      <img src="@/assets/greencloudlogo.png" alt="Logo" class="logo" />
    </div>
  </header>
</template>

<script>
export default {
  name: 'AppHeader'
}
</script>

<style>
.header {
  display: flex;
  align-items: center;
  background-color: #333;
  color: #fff;
  padding: 5px;
  padding-left: 20px;
  padding-right: 20px;
  /* padding: 0.5rem 2rem; */
  justify-content: space-between;
}

.logo {
  /* padding-left: 50rem; */
  height: 50px;
  width: auto;
}
</style>

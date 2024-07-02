<template>
  <div class="about">
    <h1>This is an about page</h1>
    <p>{{ info.data }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      info: null
    }
  },
  mounted() {
    axios.get('http://localhost:8080/my_response').then((response) => {
      this.info = response
    })
  }
}
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

<template>
  <div class="container p-2" id="app">
    <!-- Side Bar -->
    <div class="col-2">
    </div>

    <!-- Main Body -->
    <div class="col-8">
      <GenerateReport/>
    </div>

    <!-- Second Part -->
    <div class="col-2">
    </div>
  </div>
</template>

<script>
import GenerateReport from './components/GenerateReport.vue'

export default {
  name: 'App',
  components: {
    GenerateReport
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}

/* Additional styling if needed for the two parts */
#app > div {
  margin-bottom: 20px; /* Adjust as needed */
}
</style>
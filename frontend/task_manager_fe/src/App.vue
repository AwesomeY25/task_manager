<template>
  <div class="container my-2" id="app">
    <div class="row">
       <!-- Second Part -->
       <div class="col-2">
        <h2> </h2>
       </div>

        <!-- Main Body -->
        <div class="col-8">
          <InternForm/>
        </div>

       <!-- Second Part -->
       <div class="col-2">
        <h2> </h2>
      </div>
    </div>
  </div>
</template>

<script>
import InternForm from './components/InternForm.vue'

export default {
  name: 'App',
  components: {
    InternForm
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
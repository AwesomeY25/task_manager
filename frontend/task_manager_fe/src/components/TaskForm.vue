<template>
    <div class="col-8 align-items-center">
        <div class="row m-2">
            <div class="col">
                <label for="fname">First name:</label><br>
                <input type="text" id="fname" name="fname"><br>
            </div>
        </div>
        <div class="row m-2">
            <div class="col">
                <label for="lname">Last name:</label><br>
                <input type="text" id="lname" name="lname">
            </div>
        </div>
        <div class="row m-2">
            <div class="col">
                <label for="midinitial">Middle Initial:</label><br>
                <input type="text" id="midinitial" name="midinitial">
            </div>
        </div>
        <!-- Birthday -->
        <div class="row m-2">
            <div class="col">
                <label for="dept">Choose a Department:</label><br>
                <select id="dept" name="department">
                <option value="1">Finance</option>
                <option value="2">IT</option>
                <option value="3">Human Resources</option>
                <option value="4">Operations</option>
                </select>
            </div>
        </div>
        <input type="submit" value="Submit">
    </div>
</template>

<script>
export default {
  name: 'TaskForm',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>
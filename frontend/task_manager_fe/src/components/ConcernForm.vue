<template>
    <div class="container">
        <div class="container" id="header">
            <h1>Verafede Interns Concern Form</h1>
            <h3 class="mt-4">Concerns</h3>
        </div>
        <form @submit.prevent="submitForm">
            <div class="mt-4 px-2" id="q1">
                <label for="issues" class="form-label">Were there any issues/problems regarding your assigned tasks?*</label>
                <select class="form-select" id="issues" name="issues" required>
                    <option selected>Select</option>
                    <option value="1">Yes</option>
                    <option value="2">No</option>
                </select>
            </div>

            <div class="mt-5 px-2" id="q2">
                <label for="issues_enumerated" class="form-label">If yes, what were they?*</label>
                <textarea class="form-control" rows="5" placeholder="Write N/A if previous answer is no." id="issues_enumerated" name="issues_enumerated" required></textarea>
            </div>

            <div class="mt-5 px-2" id="q3">
                <label for="acad_workload" class="form-label">Do you have any academic workload at the moment?*</label>
                <div class="form-check">
                    <input class="form-check-input" type="radio" id="acad_workload1" name="acad_workload" required>
                    <label class="form-check-label" for="acad_workload1">Yes (taking full semester)</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" id="acad_workload2" name="acad_workload" required>
                    <label class="form-check-label" for="acad_workload2">Yes (taking few classes only)</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" id="acad_workload3" name="acad_workload" required>
                    <label class="form-check-label" for="acad_workload3">No</label>
                </div>
            </div>

            <div class="mt-5 px-2" id="q4">
                <label for="commitments" class="form-label">Do you have any other commitments besides your academics and Verafede?</label>
                <textarea class="form-control" rows="4" placeholder="Write N/A if none." id="commitments" name="commitments"></textarea>
            </div>

            <div class="col mt-5 px-2" id="buttons">
                <div class="row d-inline-flex align-self-end m-2">
                    <div class="col mx-auto" id="cancel_btn">
                        <button class="btn btn-outline-primary mb-3">Cancel</button>
                    </div>
                    <div class="col mx-auto" id="submit_btn">
                        <button type="submit" class="btn btn-primary mb-3">Submit</button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
export default {
  name: 'ConcernForm',
  data() {
    return {
      formData: {
        issues: '',
        issues_enumerated: '',
        acad_workload: '',
        commitments: ''
      }
    };
  },
  methods: {
    async submitForm() {
    try {
        // Print the JSON file in the console log before submitting
        console.log('Form data:', JSON.stringify(this.formData));
        
        const response = await fetch('http://127.0.0.1:8000/new/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.formData),
        });

        if (!response.ok) {
            throw new Error('Failed to submit form');
        }

        console.log('Form submitted successfully');
        
        // Reset form after successful submission
        this.resetForm();
    } catch (error) {
        console.error('Error submitting form:', error);
    }
},

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
#header > h1 {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-weight: bold;
  text-align: center;
  color: #F27036;
  margin-top: 60px;
}
#header > h3 {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #0A0A0A;
}
#q1 > label {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-weight: bold;
}
#buttons {
  text-align: center;
}
#cancel_btn > button {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-weight: bold;
  color: #52525C;
  font-size: 14px;
  border-color: #52525C;
  width: 300px;
  height: 38px;
}
#submit_btn > button {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-weight: bold;
  color: #F8FAFC;
  font-size: 14px;
  background-color: #EA580C;
  border-color: #EA580C;
  width: 300px;
  height: 38px;
}
</style>
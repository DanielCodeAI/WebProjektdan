<template>
    <div>
      <h1>Fitness Data for {{ currentDate }}</h1>
      <form @submit.prevent="submitForm">
        <div>
          <label>Weight:</label>
          <input type="number" v-model="formData.weight" />
        </div>
        <div>
          <label>Training Type:</label>
          <input type="text" v-model="formData.trainingType" />
        </div>
        <div>
          <label>Feelings:</label>
          <input type="text" v-model="formData.feelings" />
        </div>
        <!-- Add other form fields similarly -->
  
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        formData: {
          weight: '',
          trainingType: '',
          feelings: '',
          // Add other form data fields here
        },
        currentDate: new Date().toLocaleDateString()
      };
    },
    created() {
      const savedData = localStorage.getItem('fitnessData');
      if (savedData) {
        this.formData = JSON.parse(savedData);
      }
    },
    methods: {
      saveData() {
        localStorage.setItem('fitnessData', JSON.stringify(this.formData));
      },
      submitForm() {
        const params = {
          spreadsheetId: 'YOUR_SPREADSHEET_ID',
          range: 'Sheet1!A1',
          valueInputOption: 'RAW',
          resource: {
            values: [
              [new Date().toISOString(), this.formData.weight, this.formData.trainingType]
            ]
          }
        };
        gapi.client.sheets.spreadsheets.values.append(params).then((response) => {
          console.log('Data appended to Google Sheets');
          localStorage.removeItem('fitnessData');
          alert('Data saved successfully');
        });
      }
    },
    watch: {
      formData: {
        deep: true,
        handler() {
          this.saveData();
        }
      }
    }
  };
  </script>
  
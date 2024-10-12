<template>
  <div>
    <h1>Fitness Daten</h1>
    <form @submit.prevent="saveAsFile">
      <div>
        <label>Datum:</label>
        <input type="date" v-model="formData.date" />
      </div>
      <div>
        <label>Gewicht:</label>
        <input type="number" v-model="formData.weight" />
      </div>
      <div>
        <label>Trainingsart:</label>
        <input type="text" v-model="formData.trainingType" />
      </div>
      <div>
        <label>Gefühle:</label>
        <input type="text" v-model="formData.feelings" />
      </div>
      <!-- Füge mehr Felder nach Bedarf hinzu -->
      <button type="submit">Speichern</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        date: new Date().toISOString().substr(0, 10),  // Standardmäßig das heutige Datum
        weight: '',
        trainingType: '',
        feelings: '',
      }
    };
  },
  methods: {
    // Funktion zum Speichern der Daten als JSON-Datei
    saveAsFile() {
      const fileData = new Blob([JSON.stringify(this.formData)], { type: 'application/json' });
      const url = URL.createObjectURL(fileData);
      const link = document.createElement('a');
      link.href = url;
      link.download = `fitness_data_${this.formData.date}.json`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  }
};
</script>

<style scoped>
/* Optional: Styles für das Formular */
form {
  display: flex;
  flex-direction: column;
}
label {
  margin-top: 10px;
}
button {
  margin-top: 20px;
  padding: 10px;
}
</style>

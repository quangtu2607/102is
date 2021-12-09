<template>
  <div>
    <!-- <h1 class="subtitle-1 grey--text">Processes</h1> -->

    <!-- <v-snackbar v-model="snackbar" :timeout="8000" top color="red darken-4">
      <span>An error occurred while connecting to the servers.</span>
      <v-btn text color="white" @click="snackbar = false">Close</v-btn>
    </v-snackbar> -->

    <div class="box">
      <div class="grid-item">{{teamA}}</div>
      <div class="grid-item"></div> 
      <div class="grid-item">{{teamH}}</div> 
      <div class="grid-item"><img :src="require(`@/assets/${teamA}.png`)" height="50" width="50"></div>
      <div class="grid-item"></div> 
      <div class="grid-item"><img :src="require(`@/assets/${teamH}.png`)" height="50" width="50"></div> 
    </div>
    <div class="form">
      <Form></Form>
    </div>
      <!-- <v-row wrap>
        <v-switch class="px-2 my-1 pt-5" @change="switchMyProc()" color="primary" label="Only show my processes"></v-switch>
        <v-text-field class="px-2 my-1" v-model="username" color="purple" @change="store_username()" label="Type in username to filter"></v-text-field>
        <v-spacer></v-spacer>
        <span class="grey--text pr-2 my-2" v-if="date !== ''">Last update: {{ date }}</span>
        <div class="my-1 pt-4">
          <v-btn text color="grey" class="my-0" :loading="refreshLoading" @click="refresh">
            <v-icon left>refresh</v-icon>
            <span>Refresh</span>
          </v-btn>
        </div>

      </v-row>

      <div class="my-5">
        <v-simple-table dense>
          <thead>
            <tr>
              <td><span class="font-weight-bold">Server</span></td>
              <td><span class="font-weight-bold">User</span></td>
              <td><span class="font-weight-bold">PID</span></td>
              <td><span class="font-weight-bold">CPU</span></td>
              <td><span class="font-weight-bold">Memory</span></td>
              <td><span class="font-weight-bold">Start</span></td>
              <td><span class="font-weight-bold">Time</span></td>
              <td><span class="font-weight-bold">Command</span></td>
            </tr>
          </thead>
          <tbody>
            <tr v-for="process in processList()" :key="process.pid">
              <td><span>{{ process.server }}</span></td>
              <td>
                <span v-if="process.user === username" class="purple--text">{{ process.user }}</span>
                <span v-if="process.user !== username">{{ process.user }}</span>
              </td>
              <td><span>{{ process.pid }}</span></td>
              <td><span>{{ process.cpu }}%</span></td>
              <td><span>{{ process.mem }}%</span></td>
              <td><span>{{ process.start }}</span></td>
              <td><span>{{ process.time }}</span></td>
              <td><span>{{ process.command }}</span></td>
            </tr>
          </tbody>
        </v-simple-table>
      </div> -->
  </div>
</template>

<script>
import Form from '@/components/Form.vue';

export default {
  created() {
    this.teamA = this.$route.params.teamA;
    this.teamH = this.$route.params.teamH;
  },
  mounted() {
    
  },
  components: { Form },
  data() {
    return {
      teamA: String,
      teamH: String
    }
  },
  methods: {

  }
}
</script>
<style>
    .form {
        background-color: white;
        border: 1px solid black;
        padding:10px;
        margin: auto;
        width: 60%;
    }
</style>
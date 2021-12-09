<template>
  <div class="modal" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <p>Modal body text goes here.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary">Save changes</button>
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
</template>


<script>
// import moment from 'moment'
//import db from '@/fb'

export default {
  data() {
    return {
      // title: '',
      // content: '',
      // due: null,
      // inputRules: [
      //     v => v.length >= 3 || 'Minimum length is 3 characters'
      // ],
      // loading: false,
      // dialog: false
    }
  },
  methods: {
    submit() {
      // if(this.$refs.form.validate()) {
      //   this.loading = true;

      //   const project = {
      //     title: this.title,
      //     content: this.content,
      //     due: this.formattedDate,
      //     person: 'The Net Ninja',
      //     status: 'ongoing'
      //   }
      //   console.log(project);
      //   this.loading = false;
      //   this.dialog = false;
      //   this.$emit('projectAdded');
      //   //db.collection('projects').add(project).then(() => {
      //     //console.log('added to db')
      //   //})

      // }
    },
  }, computed: {
    // formattedDate() {
    //   return this.due ? moment(this.due).format("Do MMMM YYYY") : "";
    // }
  }
}
</script>
<template>
  <form>
    <!-- <v-text-field
      v-model="name"
      :error-messages="nameErrors"
      :counter="10"
      label="Name"
      required
      @input="$v.name.$touch()"
      @blur="$v.name.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="email"
      :error-messages="emailErrors"
      label="E-mail"
      required
      @input="$v.email.$touch()"
      @blur="$v.email.$touch()"
    ></v-text-field>
    <v-select
      v-model="select"
      :items="items"
      :error-messages="selectErrors"
      label="Item"
      required
      @change="$v.select.$touch()"
      @blur="$v.select.$touch()"
    ></v-select>
    <v-checkbox
      v-model="checkbox"
      :error-messages="checkboxErrors"
      label="Do you agree?"
      required
      @change="$v.checkbox.$touch()"
      @blur="$v.checkbox.$touch()"
    ></v-checkbox> -->
    <v-text-field
      v-model="fthg"
      label="FTHG"
      required
    ></v-text-field>

    <v-text-field
      v-model="ftag"
      label="FTAG"
      required
    ></v-text-field>

    <v-text-field
      v-model="hs"
      label="HS"
      required
    ></v-text-field>

    <v-text-field
      v-model="as"
      label="AS"
      required
    ></v-text-field>

    <v-text-field
      v-model="hst"
      label="HST"
      required
    ></v-text-field>


    <v-text-field
      v-model="ast"
      label="AST"
      required
    ></v-text-field>


    <v-text-field
      v-model="hf"
      label="HF"
      required
    ></v-text-field>


    <v-text-field
      v-model="af"
      label="AF"
      required
    ></v-text-field>


    <v-text-field
      v-model="hc"
      label="HC"
      required
    ></v-text-field>


    <v-text-field
      v-model="ac"
      label="AC"
      required
    ></v-text-field>


    <v-text-field
      v-model="hy"
      label="HY"
      required
    ></v-text-field>

    <v-text-field
      v-model="ay"
      label="AY"
      required
    ></v-text-field>


    <v-text-field
      v-model="hr"
      label="HR"
      required
    ></v-text-field>

    <v-text-field
      v-model="ar"
      label="AR"
      required
    ></v-text-field>



    <v-btn
      class="mr-4"
      @click="submit"
    >
      submit
    </v-btn>
    <v-btn @click="clear">
      clear
    </v-btn>
  </form>
</template>
<script>
import { validationMixin } from 'vuelidate'
//   import { required, maxLength, email } from 'vuelidate/lib/validators'
import axios from 'axios';

  export default {
    mixins: [validationMixin],

    validations: {
    //   name: { required, maxLength: maxLength(10) },
    //   email: { required, email },
    //   select: { required },
    //   checkbox: {
    //     checked (val) {
    //       return val
    //     },
    //   },
    },
    updated() {
        
    },

    data: () => ({
        fthg: 0,
        ftag: 0,
        hs: 0,
        as: 0,
        hst: 0,
        ast: 0,
        hf: 0,
        af: 0,
        hc: 0,
        ac: 0,
        hy: 0,
        ay: 0,
        hr: 0,
        ar: 0
    }),

    computed: {
    //   checkboxErrors () {
    //     const errors = []
    //     if (!this.$v.checkbox.$dirty) return errors
    //     !this.$v.checkbox.checked && errors.push('You must agree to continue!')
    //     return errors
    //   },
    //   selectErrors () {
    //     const errors = []
    //     if (!this.$v.select.$dirty) return errors
    //     !this.$v.select.required && errors.push('Item is required')
    //     return errors
    //   },
    //   nameErrors () {
    //     const errors = []
    //     if (!this.$v.name.$dirty) return errors
    //     !this.$v.name.maxLength && errors.push('Name must be at most 10 characters long')
    //     !this.$v.name.required && errors.push('Name is required.')
    //     return errors
    //   },
    //   emailErrors () {
    //     const errors = []
    //     if (!this.$v.email.$dirty) return errors
    //     !this.$v.email.email && errors.push('Must be valid e-mail')
    //     !this.$v.email.required && errors.push('E-mail is required')
    //     return errors
    //   },
    },

    methods: {
        submit () {
            // var self = this;
            axios({
                method: 'post',
                url: 'http://127.0.0.1:80/predict',
                data: {
                    FTHG: this.fthg,
                    FTAG: this.ftag,
                    HS: this.hs,
                    AS: this.as,
                    HST: this.hst,
                    AST: this.ast,
                    HF: this.hf,
                    AF: this.af,
                    HC: this.hc,
                    AC: this.ac,
                    HY: this.hy,
                    AY: this.ay,
                    HR: this.hr,
                    AR: this.ar,
                }
            });
        },
        clear () {
            this.$v.$reset()
            this.fthg = null
            this.ftag = null,
            this.hs = null,
            this.as = null,
            this.hst = null,
            this.ast = null,
            this.hf = null,
            this.af = null,
            this.hc = null,
            this.ac = null,
            this.hy = null,
            this.ay = null,
            this.hr = null,
            this.ar = null
        },
    },
  }
</script>
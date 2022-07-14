<template>
    <div class="reservation">
        <b-row>
          <b-col class="col-6">
            <p class="fs-7"><b>Reserviere deinen Tisch</b></p>
            <b-form @submit="createContact" @reset="">

              <b-form-group id="input-group-1" label="" label-for="input-1">
                <b-form-select v-model="form.restaurant" :options="optionsRestaurant"></b-form-select>
              </b-form-group>

              <b-form-group id="input-group-2" label="" label-for="input-2">
                <b-form-select v-model="form.table" :options="optionsTable"></b-form-select>
              </b-form-group>

              <b-form-group id="input-group-3" label="" label-for="input-3">
                <b-form-input
                  id="input-3"
                  v-model="form.name"
                  placeholder="Name"
                  required
                ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-5" label="" label-for="input-5">
                <b-form-input
                  id="input-5"
                  v-model="form.email"
                  placeholder="Email"
                  required
                ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-6" label="" label-for="input-6">
                <b-form-input
                  id="input-6"
                  v-model="form.phone"
                  placeholder="Telefon"
                  required
                ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-7" label="" label-for="input-7">
                <b-form-input
                  id="input-7"
                  v-model="form.message"
                  placeholder="Nachricht"
                  required
                ></b-form-input>
              </b-form-group>


              <b-form-group id="input-group-8">
                <b-form-checkbox-group
                  v-model="form.checked"
                  id="checkboxes-4"
                >
                  <b-form-checkbox value="me">Hiermit akzeptiere ich die Datenschutzrichtlinien der Restaurant GmbH</b-form-checkbox>
                </b-form-checkbox-group>
              </b-form-group>

              <b-button type="submit" variant="primary">Senden</b-button>
            </b-form>
          </b-col>
          <b-col class="col-6 d-flex align-items-center justify-content-center">
            <p class="fs-7"><b>Weitere Fragen?</b><br />Rufen Sie gerne an!</p>
          </b-col>
      </b-row>
    </div>
</template>

<script>
  export default {
    props: {
    },
    data() {
      return {
        mountains: [],
        form: {
          name: "",
          email: "",
          phone: "",
          message: "",
          checked: "",
          restaurant: null,
          table: null
        },
        optionsRestaurant: [
          { value: null, text: 'In welchem Restaurant' },
          { value: 'R1', text: 'Restaurant 1' },
          { value: 'R2', text: 'Restaurant 2' }
        ],
        optionsTable: [
          { value: null, text: 'An welchem Tisch' },
          { value: 'T1', text: 'Tisch (2 Plätze)' },
          { value: 'T2', text: 'Tisch (4 Plätze)' },
          { value: 'T3', text: 'Tisch (8 Plätze)' }
        ]
      }
    },
    async fetch() {
      
    },
    methods: {
      createReservation() {
        var serialized = this.Contact.jsonApi().serialize(this.form)
        this.Restaurant.jsonApi().create(serialized)
          .then(() => {
            console.log("Cool")
          })
      }
    },
    computed: {
      Restaurant() {
        return this.$store.$db().model('Contact')
      },
    }
  }
</script>

<style lang="sass" scoped>
    
</style>
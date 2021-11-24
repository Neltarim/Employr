<template>
  <div class="">
    <!-- Imports --> 
    <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css" integrity="sha512-YWzhKL2whUzgiheMoBFwW8CKV4qpHQAEuvilg9FAn5VJUDwKZZxkJNuGM4XkWuk94WCrrwslk8yWNGmY1EduTA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <!-- -->    


  <div class="w-full">
    <EmployeesList :employees="employees" :show="show" :edit="edit"></EmployeesList>
    <EmployeeDesc v-if="!edit" :employee="employees[show]"></EmployeeDesc>
    <AddEmployee v-else></AddEmployee>
  </div>

  </div>
</template>

<script>
import EmployeesList from './components/EmployeesList.vue'
import EmployeeDesc from './components/EmployeeDesc.vue'
import AddEmployee from './components/AddEmployee.vue'
//import request from './requests.js'


export default {
  name: 'App',
  components: {EmployeesList, AddEmployee, EmployeeDesc},

  data: () => { 
    return {
      employees: [
            {
              "name": "Mike",
              "last_name": "Taylor",
              "birthday": "01/12/1996",
              "company_entrance": "05/10/2020",
              "skills": [
                  {
                      "name": "algo",
                      "level": "2"
                  }
              ]
          },
          {
              "name": "Mike",
              "last_name": "Baiweri",
              "birthday": "01/12/1996",
              "company_entrance": "05/10/2020",
              "skills": [
                  {
                      "name": "algo",
                      "level": "4"
                  }
              ]
          }
      ],
      
      show: 0,
      edit: false,
    }
  },

  methods: {
    start_edit() {this.edit = true; this.show = this.employees.lengh},
    switch_to(index) {
      if (this.edit) {this.edit = false}
      this.show = index
    }
  },

  mounted() {
    //this.employees = request('list', 'GET')
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>

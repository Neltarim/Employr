<template>
  <div class="w-full  m-2 bg-gray-100 flex">
    <div v-on:click="switch_to(index)" v-for="(empl, index) in employees" :key="index" 
      class=" m-2 p-6 bg-gray-200" :class="{'bg-blue-400' : show == index}">
      <div class="">{{empl.name}}</div>
      <div class="">{{empl.last_name}}</div>
    </div>

    <div v-on:click="start_edit()" class="m-2 p-6 bg-gray-200" :class="{'bg-blue-400' : edit}">
      <i class="fas fa-plus"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EmployeesList',
  props: ['employees', 'show', 'edit'],

  methods: {
    start_edit()    {this.$parent.start_edit()},
    switch_to(index) {this.$parent.switch_to(index)},
  }
}
</script>
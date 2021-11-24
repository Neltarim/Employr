<template>

  <div class="bg-gray-100 m-2 p-6 flex justify-between">

    <div class="m-4">
      <p class="">{{employee.name}}</p>
      <p class="">{{employee.last_name}}</p>

    </div>

    <div class="m-4">
      <div v-for="skill in employee.skills" :key="skill" class="">
        <p class="">{{skill.name}}</p>
        <i v-for="i in 5" :key="i" class="fas fa-star text-gray-400" :class="{'text-indigo-400' : i <= skill.level}"></i>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'EmployeeDesc',
  props: ['employee'],
}
</script>
<template>
        <div class="row">
            <experience-item class="col col-12 col-lg-6 my-4 px-4 d-flex justify-content-sm-center" v-for="item in 5" :key="item"/>
        </div>
  </template>
  
  <script>
import ExperienceItem from './ExperienceItem.vue'
  export default {
  components: { ExperienceItem },
      name:"ExperienceList"
  }
  </script>
  
  <style>
   @media screen and (min-width:1141px) {
    .exp-length{
        width: 1150px;
    }
    
}
@media screen and (max-width:1141px) {
    .exp-length{
        width: 100%;
    }
}
  </style>
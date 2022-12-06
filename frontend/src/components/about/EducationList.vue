<template>
        <div class="row">
            <education-item class="col col-12 col-sm-6 my-4 px-4 d-flex justify-content-sm-center" v-for="item in 5" :key="item"/>
        </div>
  </template>
  
  <script>
import EducationItem from './EducationItem.vue'
  export default {
  components: { EducationItem },
      name:"EducationList"
  }
  </script>
  
  <style>
   @media screen and (min-width:1141px) {
    .edu-length{
        width: 1580px;
    }
    
}
@media screen and (max-width:1141px) {
    .edu-length{
        width: 100%;
    }
}
  </style>
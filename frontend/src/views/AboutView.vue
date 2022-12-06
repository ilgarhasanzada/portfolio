<template>
  <div class="about mb-5 pb-5">
    <!-- About Me -->
    <div class="text-sm-center w-100">
      <h3 class="position-absolute z-index-1 w-100 ps-3 mt-5"><span class="text-light">ABOUT</span> <span class="text-red">ME</span></h3>
      <h1 class="position-relative z-index-2 w-100 mt-5">RESUME</h1>
    </div>
    
    <!-- Personal Info -->
    <div class="container-lg">
      <h4 class="text-light d-lg-none my-4 mt-5 pt-5 mt-sm-0">PERSONAL INFOS</h4>
      <div class="row">
        <div class="col col-12 mb-sm-4 col-lg-6 d-flex justify-content-center justify-content-sm-start">
          <personal-image/>
        </div>
        <div class="col  col-12 col-lg-6 mt-lg-5 d-flex justify-content-center">
          <personal-info/>
        </div>
      </div>
      
      <hr class="m-5">
      <h3 class="text-light text-sm-center ms-3 ms-sm-0 ">MY SKILLS</h3>
      <!-- Skills -->
      <skills-vue/>
      <hr class="m-5">
      <h3 class="text-light text-sm-center ms-3 ms-sm-0">EDUCATION</h3>
      <!-- Education -->
      <education-list/>
      <hr class="m-5">
      <h3 class="text-light text-sm-center ms-3 ms-sm-0">EXPERIENCE</h3>
      <!-- Experience -->
      <experience-list/>
    </div>
  </div>
</template>
<script>
import SkillsVue from '@/components/about/Skills.vue'
import PersonalInfo from '@/components/about/PersonalInfo.vue'
import PersonalImage from '@/components/about/PersonalImage.vue'
import EducationList from '@/components/about/EducationList.vue'
import ExperienceList from '@/components/about/ExperienceList.vue'
export default {
  components: { PersonalInfo,PersonalImage,SkillsVue,EducationList,ExperienceList},
  name:"AboutView",
}
</script>

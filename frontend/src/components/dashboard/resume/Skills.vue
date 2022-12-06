<template>
    <div class="bg-dark w-100 h-100 p-3 mt-lg-0 mt-4">
        <h2>Skills</h2>
        <div class="row">
            <update-skill v-for="i in skills" :key="i" class="col col-6 col-md-4 my-3" :skill="i"/>
        </div>
    </div>
</template>

<script>

import { mapGetters } from 'vuex'
import UpdateSkill from './UpdateSkill.vue'
export default {
  components: {UpdateSkill },
    name:"SkillView",
 
  
    computed:{
        ...mapGetters({
            skills:"getSkills"
        })
    }
}
</script>

<style>

</style>
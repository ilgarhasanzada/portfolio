<template>
        <div class="row">
            <skill-vue v-for="i in skills" :key="i" class="col col-6 col-md-3 my-3" :language="i.language" :persentage=i.persentage />
        </div>
</template>

<script>
import SkillVue from '@/components/about/Skill.vue'
export default {
    name:"SkillsVue",
    components:{SkillVue},
    data(){
        return{
            skills:[
                {
                    "language":"HTML",
                    "persentage":95
                },
                {
                    "language":"CSS",
                    "persentage":80,
                    
                },
                {
                    "language":"JS",
                    "persentage":90
                },
                {
                    "language":"PYTHON",
                    "persentage":25,
                    
                },
                {
                    "language":"JAVA",
                    "persentage":10
                },
                {
                    "language":"DJANGO",
                    "persentage":75
                },
                
            ]
        }
    },
}
</script>

<style>
    @media screen and (min-width:1141px) {
    .skill-length{
        width: 1124px;
    }
    
}
@media screen and (max-width:1141px) {
    .skill-length{
        width: 100%;
    }
}
/* .skill-width{
    width: 80%;
} */
</style>
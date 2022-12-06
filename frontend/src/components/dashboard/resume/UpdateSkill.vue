<template>
  <div>
    <div class="position-relative skill" style="margin-bottom:150px !important;">
      <div class="position-absolute w-100">
        <svg viewBox="0 0 36 36" class="circular-chart orange">
            <path class="circle-bg"
                d="M18 2.0845
                a 15.9155 15.9155 0 0 1 0 31.831
                a 15.9155 15.9155 0 0 1 0 -31.831"
            />
            <path class="circle"
                :stroke-dasharray="per+',100'"
                d="M18 2.0845
                a 15.9155 15.9155 0 0 1 0 31.831
                a 15.9155 15.9155 0 0 1 0 -31.831"
            />
            <text x="18" y="20.35" class="percentage">{{per}}%</text>
        </svg><div class="text-light text-center">{{lan}}</div>
      </div>
      <div class="position-absolute w-100 d-flex justify-content-end pe-2 opacity-0 detail">
        <div class="mx-2">
          <svg @click="edit_skill($event)"  fill="white" xmlns="http://www.w3.org/2000/svg" width="17" height="24" viewBox="0 0 24 24"><path d="M22 15v2h-1v-14h-14v-1h2v-2h-6v3h-3v2h3v16h16v3h2v-3h3v-6h-2zm-3 2h-1v-2h-2v2h-1v-2h-2v2h-1v-2h-2v2h-1v-2h-2v-1h2v-2h-2v-1h2v-2h-2v-1h2v-2h-2v-1h12v12z"/></svg>
        </div>
        <div> 
          <svg @click="delete_skill()" fill="white" xmlns="http://www.w3.org/2000/svg" width="17" height="24" viewBox="0 0 24 24"><path d="M23.954 21.03l-9.184-9.095 9.092-9.174-2.832-2.807-9.09 9.179-9.176-9.088-2.81 2.81 9.186 9.105-9.095 9.184 2.81 2.81 9.112-9.192 9.18 9.1z"/></svg>
        </div>
      </div>
    </div>
    <div>
    </div>
    <div class="position-absolute bg-yellow rounded p-2" v-if="((windows_width-x)>100)" style="z-index:1000" :style="{'top':y+'px','left':x+'px'}"> 
          <div>
            <input type="text" v-model="per" class="my-2 form-control">
          </div>
          <div>
            <input type="text" v-model="lan" class="my-2 form-control">
          </div>
          <div class="d-flex justify-content-end">
            <button @click="close_skill()" class="btn btn-secondary me-2">Close</button>
            <button @click="save_language()" class="btn btn-dark">Save</button>
          </div>
    </div>
    <div class="position-absolute bg-yellow rounded p-2" v-else style="z-index:1000" :style="{'top':y+'px','right':windows_width-x+'px'}"> 
          <div>
            <input type="text" v-model="per" class="my-2 form-control">
          </div>
          <div>
            <input type="text" v-model="lan" class="my-2 form-control">
          </div>
          <div class="d-flex justify-content-end">
            <button @click="close_skill()" class="btn btn-secondary me-2">Close</button>
            <button @click="save_language()" class="btn btn-dark">Save</button>
          </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
export default {
    name:"UpdateSKill",
    props:{
        skill:Object
    },
    data(){
        return{
            lan:"",
            per:"",
            x:-500,
            y:-500
        }
    },
    methods:{
      close_skill(){
        this.x=-500
        this.y=-500
      },
        edit_skill(e){
            this.x=e.pageX;
            this.y=e.pageY;
        },
      ...mapActions({
        "deleteSkill":"actionDeleteSkill"
      }),
      delete_skill(){
        this.deleteSkill(this.skill)
      },
        save_persentage(){
            console.log(this.skill.persentage)
        },
         save_language(){
            // console.log(this.lan)
            const arr={
                "skill":this.skill,
                "lang":this.lan
            }
            try{
              this.$store.commit("updateSkill",arr)  
               axios.put("about/skills/"+this.skill.id+"/",
              {"name":this.lan,"persentage":this.per}
              )
            }catch(error){
                console.log(error)
            }
            this.x=-500
            this.y=-500
            console.log(arr)
            
        }
    },
    computed:{
      windows_width(){
        return window.innerWidth
      }
    }
    ,
    created(){
        this.lan=this.skill.name,
        this.per=this.skill.persentage
    }
}
</script>

  
<style>
.skill:hover .detail{
  opacity: 1 !important;
}
.detail{
  transition: .5s;
}
.detail div{
  cursor: pointer !important;
}
.circular-chart {
  display: block;
  margin: 10px auto;
  max-width: 80%;
  max-height: 130px;
}

.circle-bg {
  fill: none;
  stroke: #2b2a2a;
  stroke-width: 3.8;
}

.circle {
  fill: none;
  stroke-width: 2.8;
  stroke-linecap: round;
  animation: progress 1s ease-out forwards;
}

@keyframes progress {
  0% {
    stroke-dasharray: 0 100;
  }
}

.circular-chart.orange .circle {
  stroke: var(--my-red);
}

.circular-chart.green .circle {
  stroke: #4CC790;
}

.circular-chart.blue .circle {
  stroke: #3c9ee5;
}

.percentage {
  fill: #fff;
  font-family: sans-serif;
  font-size: 0.5em;
  text-anchor: middle;
}
@media screen and (max-width: 991px) {
.circular-chart {
  max-height: 100px;
} 
}
</style>
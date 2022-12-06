<template>
    <div class="d-flex bg-dark flex-column align-items-center justify-content-center">
        
        <div v-if="alert_success" class="alert alert-success fixed-top alert-dismissible fade show" role="alert">
            <button @click="alert_close" type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        
            <strong>Hey, admin!</strong> Your personal information updated!
        </div>
        <div v-if="alert_not_success" class="fixed-top">
            <div :key="(error,value)" v-for="error,value in info_error.data"  class="alert alert-danger alert-dismissible fade show" role="alert" >
                <button @click="alert_close" type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            
                <strong>Hey, admin!</strong> <span class="text-capitalize">{{value}}: </span><span class="text-capitalize">{{error["0"]}}</span>!
             </div>
        </div>
        
        <div class="about-image mt-5 mx-5 position-relative" v-for="info in about" :key="info">
            <img :src="info.image" class="w-100 h-100 position-absolute" alt="">
            <div class="w-100 h-100 bg-black position-absolute opacity-0 d-flex justify-content-center align-items-center">
                <label for="img" class="form-label  cursor-pointer"><span><svg fill="red" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M5 4h-3v-1h3v1zm8 6c-1.654 0-3 1.346-3 3s1.346 3 3 3 3-1.346 3-3-1.346-3-3-3zm11-5v17h-24v-17h5.93c.669 0 1.293-.334 1.664-.891l1.406-2.109h8l1.406 2.109c.371.557.995.891 1.664.891h3.93zm-19 4c0-.552-.447-1-1-1s-1 .448-1 1 .447 1 1 1 1-.448 1-1zm13 4c0-2.761-2.239-5-5-5s-5 2.239-5 5 2.239 5 5 5 5-2.239 5-5z"/></svg></span><span class="text-red"> Change Photo</span></label>
                <input ref="file" @change="show_image" type="file" class="form-control d-none" name="" id="img" placeholder="" aria-describedby="fileHelpId">
            </div>
        
        </div>
        <form class="my-5 px-3"  v-for="info in about" :key="info">
            <div class="d-flex">
                <div class="mb-3 me-3">
                    <label for="first_name" class="form-label">First name</label>
                    <input type="text" v-model="info.first_name" class="form-control bg-black text-light" name="" id="first_name" aria-describedby="helpId" placeholder="First name">
                </div>
                <div class="mb-3">
                    <label for="last_name" class="form-label">Last name</label>
                    <input type="text" v-model="info.last_name" class="form-control  bg-black text-light" name="" id="last_name" aria-describedby="helpId" placeholder="Last name">
                </div>
            </div>
            <div class="mb-3">
              <label for="Description" class="form-label">Description</label>
              <textarea v-model="info.description" class="form-control  bg-black text-light" placeholder="Description" name="" id="Description" rows="3"></textarea>
            </div>
            <div class="d-flex">
                <div class="mb-3 me-3">
                    <label for="Age" class="form-label">Age</label>
                    <input type="number" v-model="info.age" class="form-control  bg-black text-light" name="" id="Age" aria-describedby="helpId" placeholder="Age">
                </div>
                
                <div class="mb-3">
                    <label for="Nationally" class="form-label">Nationally</label>
                    <input type="text" v-model="info.nationality" class="form-control  bg-black text-light" name="" id="Nationally" aria-describedby="helpId" placeholder="Nationally">
                </div>
            </div>
            <div class="form-check my-3">
                <label class="form-check-label" for="freelancer">
                    Freelancer
                </label>
                <input class="form-check-input" v-model="info.freelance" type="checkbox" value="" id="freelancer">
            </div>
            <div class="d-flex">
                <div class="mb-3 me-3">
                    <label for="Adress" class="form-label">Adress</label>
                    <input type="text" v-model="info.adress" class="form-control  bg-black text-light" name="" id="Adress" aria-describedby="helpId" placeholder="Adress">
                </div>
                <div class="mb-3">
                    <label for="adress_point" class="form-label">Adress point</label>
                    <input type="text" v-model="info.adress_point" class="form-control  bg-black text-light" name="" id="adress_point" aria-describedby="helpId" placeholder="Adress point">
                </div>
            </div>
            <div class="d-flex">
                <div class="mb-3 me-3">
                    <label for="phone" class="form-label">Phone</label>
                    <input type="text" v-model="info.phone" class="form-control  bg-black text-light" name="" id="phone" aria-describedby="helpId" placeholder="Phone">
                </div>
                <div class="mb-3">
                    <label for="Email" class="form-label">Email</label>
                    <input type="email" v-model="info.email" class="form-control  bg-black text-light" name="" id="Email" aria-describedby="helpId" placeholder="Email">
                </div>
            </div>
            <div>
                <div class="d-grid gap-2">
                  <button @click="save()" type="button" name="" id="" class="btn bg-secondary">Save</button>
                </div>
            </div>
        </form>
    </div> 
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';
export default {
    name: "AboutView",
    data(){
        return{
            alert_success:false,
            alert_not_success:false,
            info_error:[],
        }
    },
    methods:{
        async show_image(event){
           let image= event.target.files[0]
           const reader = new FileReader()
            reader.readAsDataURL(image)
            reader.onload=e=>{
                image=e.target.result            
            }
            const config = {
              header: { "content_type": "multipart/form-data" }
            }
            let formData = new FormData();
            formData.append("image",image)
            try{
                this.$store.commit("updateAboutImage",image)
                await axios.patch('about/'+this.about[0].id+"/",formData,config)
            this.alert_success=true
            this.alert_not_success=false
            }catch(error){
                this.info_error=error.response
                this.alert_not_success=true
                console.log(error.response.data)
            }
            
        },

    

        alert_close(){
            if(this.alert_success){
                this.alert_success=false
            }
            if(this.alert_not_success){
                this.alert_not_success=false
            }
        },
        async save(){
            try{
            this.$store.commit("updateAbout",this.about[0])
            await axios.patch('about/'+this.about[0].id+"/",{
                "first_name": this.about[0].first_name,
                "last_name": this.about[0].last_name,
                "description": this.about[0].description,
                "age": this.about[0].age,
                "nationality": this.about[0].nationality,
                "freelance": this.about[0].freelance,
                "adress": this.about[0].adress,
                "adress_point": this.about[0].adress_point,
                "phone": this.about[0].phone,
                "email": this.about[0].email
            })
            this.alert_success=true
            this.alert_not_success=false
            }catch(error){
                this.info_error=error.response
                this.alert_not_success=true
                console.log(error.response.data)
            }
        }
    },
    computed:{
        ...mapGetters({
            about:"getAbout"
        })
    },
    
}
</script>

<style>
    .about-image{
        width: 200px;
        height: 200px;
        border-radius: 100%;
        overflow: hidden;
    }
    .about-image div{
        transition: .8s;
    }
    .about-image:hover div{
        opacity: .8 !important;
    }
</style>
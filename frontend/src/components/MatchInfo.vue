<template>
    <div class="box">
        <div class="grid-item">{{teamH}}</div>
        <div class="grid-item">{{teamA}}</div> 
        <div class="grid-item">
            <i class="fa fa-clock-o" aria-hidden="true"></i>
            {{time}}
        </div> 
        <div class="grid-item"></div> 
        <div class="grid-item"><img :src="require(`@/assets/${teamH}.png`)" height="50" width="50"></div>
        <div class="grid-item"><img :src="require(`@/assets/${teamA}.png`)" height="50" width="50"></div>  
        
        <div class="grid-item"></div> 
        <div class="grid-item"></div> 
        <div class="grid-item"></div> 
        <div class="grid-item"></div> 
        <div class="grid-item"></div> 
        <div class="grid-item" style= "text-align: right;">
            <button @click="handleClick">More info <i class="fa fa-arrow-right" aria-hidden="true"></i></button>
        </div> 
    </div>
</template>
<script>
import 'font-awesome/css/font-awesome.min.css'
export default {
    props:{
        teamA: String,   
        teamH: String,
        time: String
    },
    created() {
        
    },
    data() {
        return {
            // teamALogo: "~@/assets/" + this.teamA + ".png"
        }
    },
    methods: {
        handleClick() {
            this.$router.push('/match/' + this.teamA + '/' + this.teamH);  
        }
    } 
}
</script>
<style>
    .box {
        background-color: white;
        border: 1px solid black;
        padding:10px;
        margin: auto;
        width: 60%;
        display: grid;
        grid-template-columns: auto auto auto auto;
    }
    .grid-item {
        padding:10px;
        text-align: center;
    }
</style>
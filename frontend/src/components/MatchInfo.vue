<!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
<template>
    <div class="box">
        <div class="grid-item">{{teamH}}</div>
        <div class="grid-item"></div> 
        <div class="grid-item">{{teamA}}</div> 
        <div class="grid-item">
            <i class="fa fa-clock-o" aria-hidden="true"></i>
            <div>{{time}}</div>
        </div> 
        <div class="grid-item">
            <i class="fa fa-map-marker" aria-hidden="true"></i>
            <div v-for="s in stadium" :key="s[teamH]">{{s[teamH]}}</div>
        </div> 
        <div class="grid-item"><img :src="require(`@/assets/${teamH}.png`)" height="50" width="50"></div>
        <div class="grid-item">vs</div> 
        <div class="grid-item"><img :src="require(`@/assets/${teamA}.png`)" height="50" width="50"></div>
        
        <div class="grid-item"></div> 
        <div class="grid-item"></div> 
        <div class="grid-item"></div> 
        <div class="grid-item"></div> 
        <div class="grid-item"></div> 
        <div class="grid-item"></div>
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
            stadium: [
                {
                    "Arsenal": "Emirates Stadium" 
                },
                {
                    "Man City": "Etihad Stadium" 
                },
                {
                    "Liverpool": "Anfield" 
                },
                {
                    "Chelsea": "Stamford Bridge" 
                },
                {
                    "West Ham": "London Stadium" 
                },
                {
                    "Spurs": "Tottenham Hotspur Stadium" 
                },
                {
                    "Man Utd": "Old Trafford" 
                },
                {
                    "Wolves": "Molineux Stadium" 
                },
                {
                    "Brighton": "Falmer Stadium" 
                },
                {
                    "Aston Villa": "Villa Park" 
                },
                 {
                    "Leicester": "King Power Stadium" 
                },
                {
                    "Everton": "Goodison Park" 
                },
                {
                    "Brentford": "Brentford Community Stadium" 
                },
                {
                    "Crystal Palace": "Selhurst Park" 
                },
                {
                    "Leeds": "Elland Road" 
                },
                {
                    "Southampton": "St Mary's Stadium" 
                },
                {
                    "Warford": "Vicarage Road" 
                },
                {
                    "Burnley": "Turf Moor" 
                },
                {
                    "Newcastle": "St James' Park" 
                },
                {
                    "Norwich": "Carrow Road" 
                }
            ]
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
        border: 1px hidden black;
        border-bottom: 1px solid black;
        padding:10px;
        margin: auto;
        width: 50%;
        display: grid;
        grid-template-columns: auto auto auto auto auto;
    }
    .grid-item {
        padding:1px;
        text-align: center;
    }
</style>
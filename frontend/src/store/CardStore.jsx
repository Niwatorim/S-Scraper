//stores data from each card

import {create} from 'zustand'

export const cardDataStore = create((set)=>({
    cardData:[], //array of all cards to be returned
    setCardData:(cardData)=>set({cardData}) ,//setter function for cardData
    requestData: async (request) => {
        const res = await fetch('/api/alg',{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(request)
        })
        const data = await res.json();

        set((state) => ({cardData:[...state.cardData,data.data]}))
        return {success:true, message: 'Data retrieved'}
    }


}))
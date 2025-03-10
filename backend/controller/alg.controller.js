
export const question = async(req,res) =>{
    const userQuestion = req.body;
    
    try{
        //'AI algorithm + webscraping'
        



    }
    catch {error}{
        return res.status(500).json({
            success:false,
            message: `Error of ${error}`
        })
    }

};
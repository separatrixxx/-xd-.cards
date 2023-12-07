import axios from "axios";


export async function getImage(prompt: string, setErrorPrompt: (e: any) => void, setIsLoading: (e: any) => void,
    setImage: (e: any) => void) {
    setErrorPrompt(false);

    if (+prompt !== 0) {
        setIsLoading(true);

        await axios.post(process.env.NEXT_PUBLIC_DOMAIN + '/imageGeneration/generateCard', {
            text_stable_diffusion: prompt + "greeting card",
            text_image: prompt
        })
            .then(function (response) {
                setIsLoading(false);

                console.log('Чудо произошло :)');

                const mimeType = response.headers['content-type'];
                let file = new File([response.data], 'card', { type: mimeType });

                let reader = new FileReader();
                reader.readAsText(file);

                reader.onload = function() {
                    console.log(reader.result);
                };
            })
            .catch(function (error) {
                setIsLoading(false);

                console.log("Чуда не произошло: " + error);
            });
    } else {
        setErrorPrompt(true);
    }
}

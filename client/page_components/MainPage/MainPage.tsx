import styles from './MainPage.module.css';
import { Toaster } from 'react-hot-toast';
import { useRouter } from 'next/router';
import { Input } from '../../components/Input/Input';
import { useState } from 'react';
import { setLocale } from '../../helpers/locale.helper';
import { Button } from '../../components/Button/Button';
import { Header } from '../../components/Header/Header';
import { ImageDiv } from '../../components/Image/ImageDiv';


export const MainPage = (): JSX.Element => {
    const router = useRouter();

    const [prompt, setPrompt] = useState<string>('');
    const [errorPrompt, setErrorPrompt] = useState<boolean>(false);

    return (
        <>
            <Toaster
				position="top-center"
				reverseOrder={true}
				toastOptions={{
					duration: 2000,
				}}
			/>
            <Header />
            <div className={styles.wrapper}>
                <ImageDiv image='' text={setLocale(router.locale).card_appear} />
                <Input text={setLocale(router.locale).enter_holiday} value={prompt} error={errorPrompt}
                    onChange={(e) => setPrompt(e.target.value)} />
                <Button text={setLocale(router.locale).magic} onClick={() => {}} />
            </div>
        </>
    );
};
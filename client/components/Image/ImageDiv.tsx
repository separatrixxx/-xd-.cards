import { ImageDivProps } from './ImageDiv.props';
import styles from './ImageDiv.module.css';
import Image from 'next/image';
import { Htag } from '../Htag/Htag';
import cn from 'classnames';


export const ImageDiv = ({ image, text }: ImageDivProps): JSX.Element => {
	return <div className={cn(styles.imageDiv, {
        [styles.imageDivFull]: !image,
    })}>
        {
            image ? 
                <Image className={styles.image} draggable='false'
                    loader={() => image}
                    src={image}
                    alt='image'
                    width={1}
                    height={1}
                    unoptimized={true}
                    priority={true}
                />
            :
                <Htag tag='s' className={styles.text}>
                    {text}
                </Htag>
        }
    </div>
};
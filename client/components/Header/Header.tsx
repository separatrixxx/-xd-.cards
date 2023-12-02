import styles from './Header.module.css';
import Link from 'next/link';
import { useState } from 'react';
import { motion } from 'framer-motion';
import { useScrollY } from '../../hooks/useScrollY';
import { useResizeW } from '../../hooks/useResize';
import { Htag } from '../Htag/Htag';
import { LocaleChange } from '../LocaleChange/LocaleChange';
import cn from 'classnames';


export const Header = (): JSX.Element => {
    const [lastScroll, setLastScroll] = useState<number>(0);
    const [flag, setFlag] = useState<boolean>(false);

    const scrollPosition = useScrollY();
    const width = useResizeW();

    if (scrollPosition - lastScroll >= 200 && scrollPosition > lastScroll) {
        setFlag(true);
        setLastScroll(scrollPosition);
    } else if (scrollPosition < lastScroll) {
        setFlag(false);
        setLastScroll(scrollPosition);
    }

    const variants = {
        visible: {
            transform: 'translate(0%, 0%)',
        },
        hidden: {
            transform: 'translate(0%, -100%)',
        }
    };

    const variantsBlock = {
        visible: {
            height: 'fit-content',
            opacity: 1,
            transition: {
                duration: 0.3,
            }
        },
        hidden: {
            height: 0,
            opacity: 0,
            transition: {
                duration: 0.3,
            }
        }
    };

    if (width > 1024) {
        variantsBlock.visible.transition.duration = 0;
        variantsBlock.hidden.transition.duration = 0;
    }

    return (
        <motion.header className={styles.header}
            variants={variants}
            initial={flag ? 'hidden' : 'visible'}
            transition={{ duration: 0.3 }}
            animate={flag ? 'hidden' : 'visible'}>
            <Link href='/'>
                <Htag tag='m' className={cn(styles.link, styles.logo)}>[xd].cards</Htag>
            </Link>
            <LocaleChange />
        </motion.header>
    );
};
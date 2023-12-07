import { DetailedHTMLProps, HTMLAttributes } from "react";

export interface ImageDivProps extends DetailedHTMLProps<HTMLAttributes<HTMLDivElement>, HTMLDivElement> {
	image: string,
    text: string,
    isLoading: boolean,
}
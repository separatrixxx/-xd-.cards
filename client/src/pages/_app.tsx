import '../styles/globals.css';
import type { AppProps } from 'next/app';
import Head from 'next/head';
import React from 'react';


export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>[xd].cards</title>
        <meta name='description' content='[xd].cards' />
        <meta property='og:title' content='[xd].cards' />
        <meta property='og:description' content='[xd].cards' />
        <meta charSet="utf-8" />
        <link rel="icon" href="/logo.svg" type='image/svg+xml' />
      </Head>
      <Component {...pageProps} />
    </>

  );
}

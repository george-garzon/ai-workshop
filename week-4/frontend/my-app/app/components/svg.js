export function homeSVG() {
    return(
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"
             aria-hidden="true">
            <path strokeWidth="1.7"
                  d="M2.85 9.35c0-.423.218-.85.635-1.143l7.496-5.172h.001a1.84 1.84 0 0 1 2.036 0l7.495 5.17.002.002c.417.293.635.72.635 1.142V19.7c0 .73-.676 1.45-1.65 1.45h-15c-.974 0-1.65-.72-1.65-1.45z"
                  className="acf8be2bstroke"></path>
            <path stroke="currentColor" strokeLinecap="round" strokeWidth="1.7"
                  d="M17.25 15A7.86 7.86 0 0 1 12 17.002 7.86 7.86 0 0 1 6.75 15" className="acf8be2bstroke"></path>
        </svg>
    )
}

export function messagesSVG() {
    return(
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" aria-hidden="true">
            <mask id="d949a" fill="#fff">
                <path fillRule="evenodd"
                      d="M19 2a3 3 0 0 1 3 3v15.806c0 1.335-1.613 2.005-2.559 1.062L15.56 18H5a3 3 0 0 1-3-3V5a3 3 0 0 1 3-3z"
                      clipRule="evenodd"></path>
            </mask>
            <path fill="currentColor"
                  d="m19.441 21.868 1.2-1.204zM15.56 18v-1.7h.702l.498.496zM20.3 5A1.3 1.3 0 0 0 19 3.7V.3A4.7 4.7 0 0 1 23.7 5zm0 8.956V5h3.4v8.956zm0 2.544v-2.544h3.4V16.5zm0 4.306V16.5h3.4v4.306zm.341-.142a.23.23 0 0 0-.218-.043.23.23 0 0 0-.123.185h3.4c0 2.848-3.441 4.277-5.459 2.267zm-3.882-3.868 3.882 3.868-2.4 2.409-3.882-3.869zM5 16.3h10.559v3.4H5zM3.7 15A1.3 1.3 0 0 0 5 16.3v3.4A4.7 4.7 0 0 1 .3 15zm0-10v10H.3V5zM5 3.7A1.3 1.3 0 0 0 3.7 5H.3A4.7 4.7 0 0 1 5 .3zm14 0H5V.3h14z"
                  className="165c1e53fill" mask="url(#d949a)"></path>
            <path fill="currentColor" fillRule="evenodd"
                  d="M17 7a.85.85 0 0 1 0 1.7H7A.85.85 0 1 1 7 7zm-5 4a.85.85 0 0 1 0 1.7H7A.85.85 0 0 1 7 11z"
                  className="165c1e53fill" clipRule="evenodd"></path>
        </svg>
    )
}

export function helpSVG() {
    return(
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" aria-hidden="true">
            <circle cx="12" cy="12" r="9.65" stroke="currentColor" strokeWidth="1.7"
                    className="ce4eebf6stroke ce007016circle"></circle>
            <path stroke="currentColor" strokeLinecap="round" strokeWidth="1.7"
                  d="M9.664 8.576a2.41 2.41 0 1 1 4.102 2.39l-1.075 1.104c-.326.322-.765.76-.765 1.544v.364"
                  className="ce4eebf6stroke ef4f0cadnegative"></path>
            <circle cx="11.927" cy="16.884" r="0.884" fill="currentColor"
                    className="488360c7fill ef4f0cadnegative"></circle>
        </svg>
    )
}
export function caretLeft(){
    return (
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M10.85 3.99984C10.85 4.21984 10.77 4.43984 10.6 4.59984L7.20005 7.99984L10.6 11.3998C10.93 11.7298 10.93 12.2698 10.6 12.5998C10.27 12.9298 9.73005 12.9298 9.40005 12.5998L4.80005 7.99984L9.40005 3.39984C9.73005 3.06984 10.27 3.06984 10.6 3.39984C10.77 3.56984 10.85 3.77984 10.85 3.99984Z" fill="currentColor"></path></svg>
    )
}
export function caretRight(){
    return(
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M5.42773 4.70898C5.46387 4.85254 5.53809 4.98828 5.65039 5.10059L8.54932 8L5.64893 10.9004C5.31689 11.2324 5.31689 11.7705 5.64893 12.1025C5.98096 12.4336 6.51904 12.4336 6.85107 12.1025L10.3516 8.60059C10.5591 8.39355 10.6367 8.10449 10.585 7.83691C10.5537 7.67578 10.4761 7.52246 10.3516 7.39844L6.85254 3.89941C6.52051 3.56738 5.98242 3.56738 5.65039 3.89941C5.43066 4.11816 5.35645 4.42871 5.42773 4.70898Z" fill="currentColor"></path></svg>
    )
}

export function microphone(){
    return(
        <svg width="16" height="16" viewBox="-2 -1 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6 9C7.66 9 9 7.66 9 6V3C9 1.34 7.66 0 6 0C4.34 0 3 1.34 3 3V6C3 7.66 4.34 9 6 9ZM10.5 5V6C10.5 8.48 8.48 10.5 6 10.5C3.52 10.5 1.5 8.48 1.5 6V5H0V6C0 9.06 2.29 11.58 5.25 11.95V14H6.75V11.95C9.71 11.58 12 9.06 12 6V5H10.5Z" fill="#6c6f74"></path></svg>
    )
}

export function paperclipAttach(){
    return(
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path fill="currentColor" fillRule="evenodd" d="M7.67 2.507a.85.85 0 0 1 0 1.202L3.524 7.855a2.464 2.464 0 0 0 3.485 3.484l5.925-5.926a.836.836 0 0 0-1.181-1.182L5.87 10.113A.85.85 0 0 1 4.669 8.91l5.881-5.88a2.536 2.536 0 0 1 3.585 3.586L8.201 12.55a4.164 4.164 0 0 1-5.889-5.888l.006-.005 4.149-4.15a.85.85 0 0 1 1.202 0Z" clipRule="evenodd"></path></svg>
    )
}
export function arrowUp(){
    return(
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path fill="currentColor" fillRule="evenodd" d="M7.4 1.899a.85.85 0 0 1 1.201 0l4.5 4.5A.85.85 0 1 1 11.9 7.6L8.85 4.552V13.5a.85.85 0 0 1-1.7 0V4.552L4.101 7.601A.85.85 0 1 1 2.9 6.399z" clipRule="evenodd"></path></svg>
    )
}
export function caretDown(){
    return <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path fillRule="evenodd" clipRule="evenodd" d="M18.601 8.39897C18.269 8.06702 17.7309 8.06702 17.3989 8.39897L12 13.7979L6.60099 8.39897C6.26904 8.06702 5.73086 8.06702 5.39891 8.39897C5.06696 8.73091 5.06696 9.2691 5.39891 9.60105L11.3989 15.601C11.7309 15.933 12.269 15.933 12.601 15.601L18.601 9.60105C18.9329 9.2691 18.9329 8.73091 18.601 8.39897Z" fill="currentColor"></path></svg>
}
export function search(){
    return(
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><circle cx="7.5" cy="7.5" r="4.625" stroke="currentColor" strokeWidth="1.75"></circle><path d="M13.3813 14.6187C13.723 14.9604 14.277 14.9604 14.6187 14.6187C14.9604 14.277 14.9604 13.723 14.6187 13.3813L13.3813 14.6187ZM10.3813 11.6187L13.3813 14.6187L14.6187 13.3813L11.6187 10.3813L10.3813 11.6187Z" fill="currentColor"></path></svg>
    )
}
export function messageSend() {
    return (
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path fill="currentColor" fillRule="evenodd"
              d="m4.394 14.7 9.356-5.4c1-.577 1-2.02 0-2.598L4.394 1.299a1.5 1.5 0 0 0-2.25 1.3v3.438l4.059 1.088c.494.132.494.833 0 .966l-4.06 1.087v4.224a1.5 1.5 0 0 0 2.25 1.299"
              clipRule="evenodd"></path></svg>
    )
}
export function expand(){
    return(
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 16 16" aria-hidden="true"><path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.5" d="m9 7 4.5-4.5m-4 0h4v4M7 9l-4.5 4.5m4 0h-4v-4"></path></svg>
    )
}
export function shrink(){
    return(
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" transform="matrix(-1,0,0,1,0,0)"><path d="M13.59 5.31h-1.7l3.3-3.3-1.2-1.2-3.3 3.3v-1.7a.85.85 0 1 0-1.7 0v4.6h4.6a.85.85 0 1 0 0-1.7M1.57 9.84c0 .47.38.85.85.85h1.7l-3.3 3.3 1.2 1.2 3.3-3.3v1.7a.85.85 0 1 0 1.7 0v-4.6h-4.6a.85.85 0 0 0-.85.85" fill="currentColor"></path></svg>
    )
}

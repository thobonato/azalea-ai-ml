import React from 'react';
import logo from '../assets/azalealogo.svg'
import sideIcons from '../assets/sideicons.svg'

const SideNav = () => {
    return (
        <>
            <div className="flex w-12 flex-col items-center border-r-2 border-[#C2C2C2] bg-[#F6F8FC] pt-1">
                <img src={logo} alt="logo" className="w-8 h-8" />
                <div data-orientation="horizontal" role="none" className="shrink-0 h-[1px] mx-3 my-5 w-5 bg-[#6C6C6C] p-[1px]"></div>
                <div className='flex flex-col space-y-5'>
                    <img src={sideIcons} alt="sideIcons"/>
                </div>
                
            </div>
        </>
    );
};

export default SideNav;
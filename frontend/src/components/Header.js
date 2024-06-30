import React from "react";
import akim from "../assets/akim.svg";

const Header = () => {
    return (
        <div className="flex h-[50px] w-full items-center border-b-2 border-[#C2C2C2] bg-white px-7">
            <div className="flex w-full justify-between items-center text-2xl font-bold text-gray-800">
                <span className="">azalea</span>
                <img src={akim} alt="akim" className="w-10 h-10" />
            </div>
        </div>
    );
};

export default Header;
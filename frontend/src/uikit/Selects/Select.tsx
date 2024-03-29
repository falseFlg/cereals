import { darken } from "polished";
import React from "react";
import ReactSelect from "react-select";
import styled from "styled-components";

interface ISelect {
  value: string | number;
  label: string | number;
}

interface IProps {
  variant?: "light" | "dark";
  options: ISelect[];
  disabled?: boolean;
  onChange?: (value: any | any[]) => void;
}

const getBgColor = (variant: "light" | "dark") =>
  variant === "light" ? "#F5F2EA" : "#e7e2d4";

export const Select: React.FC<IProps> = ({
  options,
  variant = "dark",
  onChange,
  disabled,
  ...rest
}) => (
  <StyledReactSelect
    classNamePrefix="Select"
    options={options}
    variant={variant}
    placeholder="Выберите . . ."
    onChange={onChange}
    isDisabled={disabled}
    {...rest}
  />
);

const StyledReactSelect = styled(ReactSelect)`
  color: #333333;
  transition: 0.3s;

  .Select__value-container {
    padding-left: 20px;
  }

  .Select__control {
    cursor: pointer;
    border: 0px;
    width: 345px;
    height: 50px;
    background-color: ${({ variant }) => getBgColor(variant)};
    border-radius: 6px;
    border: 1px solid #e7e2d1;
  }

  .Select__indicator-separator {
    display: none;
  }

  .Select__menu {
    background-color: ${({ variant }) => getBgColor(variant)};
    width: 345px;
  }

  .Select__menu-list {
    padding: 0;
    border-radius: 4px;
  }

  .Select__option {
    color: #333333;
    background-color: ${({ variant }) => getBgColor(variant)};
    cursor: pointer;

    &:hover {
      background-color: ${({ variant }) => darken(0.06, getBgColor(variant))};
    }
  }
`;

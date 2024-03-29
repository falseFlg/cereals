import React from "react";
import { matchPath, NavLink, NavLinkProps } from "react-router-dom";
import styled from "styled-components";
import { TAppNavItem } from "../../routes/models";

/**
 * Модель свойств компонента.
 *
 * @prop {TAppNavItem} navItem Параметры навигации.
 * @prop {string} currentSection Название текущей секции.
 */
interface INavSidebarItemProps {
  navItem: TAppNavItem;
  currentSection: string;
}

/**
 * Компонент элемента главного меню.
 */
export const NavSidebarItem: React.FC<INavSidebarItemProps> = ({ navItem }) => {
  return (
    <StyledListItem>
      <StyledNavLink
        exact
        to={navItem.path}
        title={navItem?.element?.label}
        isActive={(_match, activeLocation) => {
          const isChosen = !!matchPath(activeLocation.pathname, {
            path: navItem.path,
            exact: false,
            strict: false,
          });
          return isChosen;
        }}
      >
        {navItem?.element?.label && <span>{navItem.element.label}</span>}
      </StyledNavLink>
    </StyledListItem>
  );
};

const StyledListItem = styled.li`
  padding-bottom: 20px;
`;

const StyledNavLink = styled(NavLink)<NavLinkProps>`
  color: #191919;
  text-decoration: none;
  transition: 0.3s;

  &.active {
    color: #407ef5;
  }
`;

import React from "react";
import { useHistory } from "react-router-dom";
import { Button, Flex, Spacer, Typography } from "../../uikit";

/**
 * Компонент с ошибкой, отображаемый при отсутствии доступа пользователя к странице
 */
export const NoPermissions = () => {
  const history = useHistory();

  /**
   * Обработчик клика по кнопке перехода к доступному функционалу
   */
  const handleButtonClick = () => {
    history.push("/");
  };

  return (
    <Flex
      column
      fillHeight
      fillWidth
      vAlignContent="center"
      hAlignContent="center"
    >
      <Spacer />
      <Typography size="sm">Нет доступа</Typography>
      <Spacer />
      <Button variant="base" onClick={handleButtonClick}>
        Перейти к доступному функционалу
      </Button>
    </Flex>
  );
};

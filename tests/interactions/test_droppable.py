import allure

from pages.interactions.page_droppable import PageDroppable


@allure.title("Тест перетаскивания объета")
def test_droppable(get_driver):
    _steps = PageDroppable(get_driver)
    _steps.step_1_transition()
    _steps.step_2_drag_and_drop()

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BORDER_EXPORT_COLOR_TABLE_METADATA = Metadata(
    id="b07356bd59a7014a0150a342d7a8af84716e878d.boutiques",
    name="border-export-color-table",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


BorderExportColorTableParameters = typing.TypedDict('BorderExportColorTableParameters', {
    "__STYX_TYPE__": typing.Literal["border-export-color-table"],
    "border_file": InputPathType,
    "table_out": str,
    "opt_class_colors": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "border-export-color-table": border_export_color_table_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class BorderExportColorTableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `border_export_color_table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def border_export_color_table_params(
    border_file: InputPathType,
    table_out: str,
    opt_class_colors: bool = False,
) -> BorderExportColorTableParameters:
    """
    Build parameters.
    
    Args:
        border_file: the input border file.
        table_out: output - the output text file.
        opt_class_colors: use class colors instead of the name colors.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "border-export-color-table",
        "border_file": border_file,
        "table_out": table_out,
        "opt_class_colors": opt_class_colors,
    }
    return params


def border_export_color_table_cargs(
    params: BorderExportColorTableParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("wb_command")
    cargs.append("-border-export-color-table")
    cargs.append(execution.input_file(params.get("border_file")))
    cargs.append(params.get("table_out"))
    if params.get("opt_class_colors"):
        cargs.append("-class-colors")
    return cargs


def border_export_color_table_outputs(
    params: BorderExportColorTableParameters,
    execution: Execution,
) -> BorderExportColorTableOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BorderExportColorTableOutputs(
        root=execution.output_file("."),
    )
    return ret


def border_export_color_table_execute(
    params: BorderExportColorTableParameters,
    execution: Execution,
) -> BorderExportColorTableOutputs:
    """
    Write border names and colors as text.
    
    Takes the names and colors of each border, and writes it to the same format
    as -metric-label-import expects. By default, the borders are colored by
    border name, specify -class-colors to color them by class instead. The key
    values start at 1 and follow the order of the borders in the file.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BorderExportColorTableOutputs`).
    """
    params = execution.params(params)
    cargs = border_export_color_table_cargs(params, execution)
    ret = border_export_color_table_outputs(params, execution)
    execution.run(cargs)
    return ret


def border_export_color_table(
    border_file: InputPathType,
    table_out: str,
    opt_class_colors: bool = False,
    runner: Runner | None = None,
) -> BorderExportColorTableOutputs:
    """
    Write border names and colors as text.
    
    Takes the names and colors of each border, and writes it to the same format
    as -metric-label-import expects. By default, the borders are colored by
    border name, specify -class-colors to color them by class instead. The key
    values start at 1 and follow the order of the borders in the file.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        border_file: the input border file.
        table_out: output - the output text file.
        opt_class_colors: use class colors instead of the name colors.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BorderExportColorTableOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BORDER_EXPORT_COLOR_TABLE_METADATA)
    params = border_export_color_table_params(
        border_file=border_file,
        table_out=table_out,
        opt_class_colors=opt_class_colors,
    )
    return border_export_color_table_execute(params, execution)


__all__ = [
    "BORDER_EXPORT_COLOR_TABLE_METADATA",
    "BorderExportColorTableOutputs",
    "BorderExportColorTableParameters",
    "border_export_color_table",
    "border_export_color_table_params",
]

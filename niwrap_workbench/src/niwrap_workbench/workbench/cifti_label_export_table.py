# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_LABEL_EXPORT_TABLE_METADATA = Metadata(
    id="8e3356d3b69610a5d7c07175dfe70d7c516f705f.boutiques",
    name="cifti-label-export-table",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


CiftiLabelExportTableParameters = typing.TypedDict('CiftiLabelExportTableParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-label-export-table"],
    "label_in": InputPathType,
    "map": str,
    "table_out": str,
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
        "cifti-label-export-table": cifti_label_export_table_cargs,
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


class CiftiLabelExportTableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_export_table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_label_export_table_params(
    label_in: InputPathType,
    map_: str,
    table_out: str,
) -> CiftiLabelExportTableParameters:
    """
    Build parameters.
    
    Args:
        label_in: the input cifti label file.
        map_: the number or name of the label map to use.
        table_out: output - the output text file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-label-export-table",
        "label_in": label_in,
        "map": map_,
        "table_out": table_out,
    }
    return params


def cifti_label_export_table_cargs(
    params: CiftiLabelExportTableParameters,
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
    cargs.append("-cifti-label-export-table")
    cargs.append(execution.input_file(params.get("label_in")))
    cargs.append(params.get("map"))
    cargs.append(params.get("table_out"))
    return cargs


def cifti_label_export_table_outputs(
    params: CiftiLabelExportTableParameters,
    execution: Execution,
) -> CiftiLabelExportTableOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiLabelExportTableOutputs(
        root=execution.output_file("."),
    )
    return ret


def cifti_label_export_table_execute(
    params: CiftiLabelExportTableParameters,
    execution: Execution,
) -> CiftiLabelExportTableOutputs:
    """
    Export label table from cifti as text.
    
    Takes the label table from the cifti label map, and writes it to a text
    format matching what is expected by -cifti-label-import.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiLabelExportTableOutputs`).
    """
    params = execution.params(params)
    cargs = cifti_label_export_table_cargs(params, execution)
    ret = cifti_label_export_table_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_label_export_table(
    label_in: InputPathType,
    map_: str,
    table_out: str,
    runner: Runner | None = None,
) -> CiftiLabelExportTableOutputs:
    """
    Export label table from cifti as text.
    
    Takes the label table from the cifti label map, and writes it to a text
    format matching what is expected by -cifti-label-import.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_in: the input cifti label file.
        map_: the number or name of the label map to use.
        table_out: output - the output text file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiLabelExportTableOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_LABEL_EXPORT_TABLE_METADATA)
    params = cifti_label_export_table_params(
        label_in=label_in,
        map_=map_,
        table_out=table_out,
    )
    return cifti_label_export_table_execute(params, execution)


__all__ = [
    "CIFTI_LABEL_EXPORT_TABLE_METADATA",
    "CiftiLabelExportTableOutputs",
    "CiftiLabelExportTableParameters",
    "cifti_label_export_table",
    "cifti_label_export_table_params",
]

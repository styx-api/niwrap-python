# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LABEL_ERODE_METADATA = Metadata(
    id="7906584e69081c776c13880cdd7ac9a11eb1e602.boutiques",
    name="label-erode",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


LabelErodeParameters = typing.TypedDict('LabelErodeParameters', {
    "__STYXTYPE__": typing.Literal["label-erode"],
    "label": InputPathType,
    "surface": InputPathType,
    "erode_dist": float,
    "label_out": str,
    "opt_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_column_column": typing.NotRequired[str | None],
    "opt_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
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
        "label-erode": label_erode_cargs,
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
        "label-erode": label_erode_outputs,
    }.get(t)


class LabelErodeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_erode(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output label file"""


def label_erode_params(
    label: InputPathType,
    surface: InputPathType,
    erode_dist: float,
    label_out: str,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
) -> LabelErodeParameters:
    """
    Build parameters.
    
    Args:
        label: the input label.
        surface: the surface to erode on.
        erode_dist: distance in mm to erode the labels.
        label_out: the output label file.
        opt_roi_roi_metric: assume values outside this roi are labeled: metric\
            file, positive values denote vertices that have data.
        opt_column_column: select a single column to erode: the column number\
            or name.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label-erode",
        "label": label,
        "surface": surface,
        "erode_dist": erode_dist,
        "label_out": label_out,
    }
    if opt_roi_roi_metric is not None:
        params["opt_roi_roi_metric"] = opt_roi_roi_metric
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if opt_corrected_areas_area_metric is not None:
        params["opt_corrected_areas_area_metric"] = opt_corrected_areas_area_metric
    return params


def label_erode_cargs(
    params: LabelErodeParameters,
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
    cargs.append("-label-erode")
    cargs.append(execution.input_file(params.get("label")))
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(str(params.get("erode_dist")))
    cargs.append(params.get("label_out"))
    if params.get("opt_roi_roi_metric") is not None:
        cargs.extend([
            "-roi",
            execution.input_file(params.get("opt_roi_roi_metric"))
        ])
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    if params.get("opt_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-corrected-areas",
            execution.input_file(params.get("opt_corrected_areas_area_metric"))
        ])
    return cargs


def label_erode_outputs(
    params: LabelErodeParameters,
    execution: Execution,
) -> LabelErodeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LabelErodeOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(params.get("label_out")),
    )
    return ret


def label_erode_execute(
    params: LabelErodeParameters,
    execution: Execution,
) -> LabelErodeOutputs:
    """
    Erode a label file.
    
    Around each vertex that is unlabeled, set surrounding vertices to unlabeled.
    The surrounding vertices are all immediate neighbors and all vertices within
    the specified distance.
    
    Note that the -corrected-areas option uses an approximate correction for
    distance along the surface.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LabelErodeOutputs`).
    """
    params = execution.params(params)
    cargs = label_erode_cargs(params, execution)
    ret = label_erode_outputs(params, execution)
    execution.run(cargs)
    return ret


def label_erode(
    label: InputPathType,
    surface: InputPathType,
    erode_dist: float,
    label_out: str,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    runner: Runner | None = None,
) -> LabelErodeOutputs:
    """
    Erode a label file.
    
    Around each vertex that is unlabeled, set surrounding vertices to unlabeled.
    The surrounding vertices are all immediate neighbors and all vertices within
    the specified distance.
    
    Note that the -corrected-areas option uses an approximate correction for
    distance along the surface.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label: the input label.
        surface: the surface to erode on.
        erode_dist: distance in mm to erode the labels.
        label_out: the output label file.
        opt_roi_roi_metric: assume values outside this roi are labeled: metric\
            file, positive values denote vertices that have data.
        opt_column_column: select a single column to erode: the column number\
            or name.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelErodeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_ERODE_METADATA)
    params = label_erode_params(
        label=label,
        surface=surface,
        erode_dist=erode_dist,
        label_out=label_out,
        opt_roi_roi_metric=opt_roi_roi_metric,
        opt_column_column=opt_column_column,
        opt_corrected_areas_area_metric=opt_corrected_areas_area_metric,
    )
    return label_erode_execute(params, execution)


__all__ = [
    "LABEL_ERODE_METADATA",
    "LabelErodeOutputs",
    "LabelErodeParameters",
    "label_erode",
    "label_erode_params",
]

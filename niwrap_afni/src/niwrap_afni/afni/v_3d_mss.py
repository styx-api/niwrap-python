# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_MSS_METADATA = Metadata(
    id="276226ad44e7a9804c89600a9895d189f8152cd2.boutiques",
    name="3dMSS",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dMssParameters = typing.TypedDict('V3dMssParameters', {
    "__STYXTYPE__": typing.Literal["3dMSS"],
    "prefix": str,
    "jobs": typing.NotRequired[float | None],
    "mrr_formula": typing.NotRequired[str | None],
    "lme_formula": typing.NotRequired[str | None],
    "random_effect": typing.NotRequired[str | None],
    "qvars": typing.NotRequired[str | None],
    "mask": typing.NotRequired[InputPathType | None],
    "bounds": typing.NotRequired[list[float] | None],
    "prediction_table": typing.NotRequired[InputPathType | None],
    "data_table": InputPathType,
    "cio_flag": bool,
    "rio_flag": bool,
    "help_flag": bool,
    "dbg_args_flag": bool,
    "if_name": typing.NotRequired[str | None],
    "show_allowed_options_flag": bool,
    "sdiff_vars": typing.NotRequired[str | None],
    "vt_formula": typing.NotRequired[str | None],
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
        "3dMSS": v_3d_mss_cargs,
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
        "3dMSS": v_3d_mss_outputs,
    }.get(t)


class V3dMssOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_mss(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file in NIfTI format"""


def v_3d_mss_params(
    prefix: str,
    data_table: InputPathType,
    jobs: float | None = None,
    mrr_formula: str | None = None,
    lme_formula: str | None = None,
    random_effect: str | None = None,
    qvars: str | None = None,
    mask: InputPathType | None = None,
    bounds: list[float] | None = None,
    prediction_table: InputPathType | None = None,
    cio_flag: bool = False,
    rio_flag: bool = False,
    help_flag: bool = False,
    dbg_args_flag: bool = False,
    if_name: str | None = None,
    show_allowed_options_flag: bool = False,
    sdiff_vars: str | None = None,
    vt_formula: str | None = None,
) -> V3dMssParameters:
    """
    Build parameters.
    
    Args:
        prefix: Output file name. For AFNI format, provide prefix only, with no\
            view+suffix needed. Filename for NIfTI format should have .nii\
            attached.
        data_table: List the data structure with a header as the first line.
        jobs: Number of CPU cores for parallel processing.
        mrr_formula: Model formulation through multilevel smoothing splines.
        lme_formula: Specify the fixed effect components of the model.
        random_effect: Specify the random effect components of the model.
        qvars: Identify quantitative variables (or covariates). The list with\
            more than one variable has to be separated with comma without any other\
            characters.
        mask: Process voxels inside this mask only.
        bounds: Outlier removal bounds. Any values in the input data that are\
            beyond the bounds will be removed and treated as missing.
        prediction_table: Provide a data table so that predicted values could\
            be generated for graphical illustration.
        cio_flag: Use AFNI's C io functions, which is default.
        rio_flag: Use R's io functions.
        help_flag: Display help message.
        dbg_args_flag: Enable R to save the parameters in a file called\
            .3dMSS.dbg.AFNI.args for debugging.
        if_name: Specify the column name that is designated for input files of\
            effect estimate. Default is 'InputFile'.
        show_allowed_options_flag: List of allowed options.
        sdiff_vars: Specify the factors for group comparisons.
        vt_formula: Specify varying smoothing terms. Two components are\
            required: the first one 'var' indicates the variable (e.g., subject)\
            around which the smoothing will vary while the second component\
            specifies the smoothing formulation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dMSS",
        "prefix": prefix,
        "data_table": data_table,
        "cio_flag": cio_flag,
        "rio_flag": rio_flag,
        "help_flag": help_flag,
        "dbg_args_flag": dbg_args_flag,
        "show_allowed_options_flag": show_allowed_options_flag,
    }
    if jobs is not None:
        params["jobs"] = jobs
    if mrr_formula is not None:
        params["mrr_formula"] = mrr_formula
    if lme_formula is not None:
        params["lme_formula"] = lme_formula
    if random_effect is not None:
        params["random_effect"] = random_effect
    if qvars is not None:
        params["qvars"] = qvars
    if mask is not None:
        params["mask"] = mask
    if bounds is not None:
        params["bounds"] = bounds
    if prediction_table is not None:
        params["prediction_table"] = prediction_table
    if if_name is not None:
        params["if_name"] = if_name
    if sdiff_vars is not None:
        params["sdiff_vars"] = sdiff_vars
    if vt_formula is not None:
        params["vt_formula"] = vt_formula
    return params


def v_3d_mss_cargs(
    params: V3dMssParameters,
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
    cargs.append("3dMSS")
    cargs.append(params.get("prefix"))
    if params.get("jobs") is not None:
        cargs.extend([
            "-jobs",
            str(params.get("jobs"))
        ])
    if params.get("mrr_formula") is not None:
        cargs.extend([
            "-mrr",
            params.get("mrr_formula")
        ])
    if params.get("lme_formula") is not None:
        cargs.extend([
            "-lme",
            params.get("lme_formula")
        ])
    if params.get("random_effect") is not None:
        cargs.extend([
            "-ranEff",
            params.get("random_effect")
        ])
    if params.get("qvars") is not None:
        cargs.extend([
            "-qVars",
            params.get("qvars")
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("bounds") is not None:
        cargs.extend([
            "-bounds",
            *map(str, params.get("bounds"))
        ])
    if params.get("prediction_table") is not None:
        cargs.extend([
            "-prediction",
            execution.input_file(params.get("prediction_table"))
        ])
    cargs.extend([
        "-dataTable",
        execution.input_file(params.get("data_table"))
    ])
    if params.get("cio_flag"):
        cargs.append("-cio")
    if params.get("rio_flag"):
        cargs.append("-Rio")
    if params.get("help_flag"):
        cargs.append("-help")
    if params.get("dbg_args_flag"):
        cargs.append("-dbgArgs")
    if params.get("if_name") is not None:
        cargs.extend([
            "-IF",
            params.get("if_name")
        ])
    if params.get("show_allowed_options_flag"):
        cargs.append("-show_allowed_options")
    if params.get("sdiff_vars") is not None:
        cargs.extend([
            "-sdiff",
            params.get("sdiff_vars")
        ])
    if params.get("vt_formula") is not None:
        cargs.extend([
            "-vt",
            params.get("vt_formula")
        ])
    return cargs


def v_3d_mss_outputs(
    params: V3dMssParameters,
    execution: Execution,
) -> V3dMssOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dMssOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix") + ".nii"),
    )
    return ret


def v_3d_mss_execute(
    params: V3dMssParameters,
    execution: Execution,
) -> V3dMssOutputs:
    """
    Voxelwise Multilevel Smoothing Spline (MSS) Analysis.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dMssOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_mss_cargs(params, execution)
    ret = v_3d_mss_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_mss(
    prefix: str,
    data_table: InputPathType,
    jobs: float | None = None,
    mrr_formula: str | None = None,
    lme_formula: str | None = None,
    random_effect: str | None = None,
    qvars: str | None = None,
    mask: InputPathType | None = None,
    bounds: list[float] | None = None,
    prediction_table: InputPathType | None = None,
    cio_flag: bool = False,
    rio_flag: bool = False,
    help_flag: bool = False,
    dbg_args_flag: bool = False,
    if_name: str | None = None,
    show_allowed_options_flag: bool = False,
    sdiff_vars: str | None = None,
    vt_formula: str | None = None,
    runner: Runner | None = None,
) -> V3dMssOutputs:
    """
    Voxelwise Multilevel Smoothing Spline (MSS) Analysis.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Output file name. For AFNI format, provide prefix only, with no\
            view+suffix needed. Filename for NIfTI format should have .nii\
            attached.
        data_table: List the data structure with a header as the first line.
        jobs: Number of CPU cores for parallel processing.
        mrr_formula: Model formulation through multilevel smoothing splines.
        lme_formula: Specify the fixed effect components of the model.
        random_effect: Specify the random effect components of the model.
        qvars: Identify quantitative variables (or covariates). The list with\
            more than one variable has to be separated with comma without any other\
            characters.
        mask: Process voxels inside this mask only.
        bounds: Outlier removal bounds. Any values in the input data that are\
            beyond the bounds will be removed and treated as missing.
        prediction_table: Provide a data table so that predicted values could\
            be generated for graphical illustration.
        cio_flag: Use AFNI's C io functions, which is default.
        rio_flag: Use R's io functions.
        help_flag: Display help message.
        dbg_args_flag: Enable R to save the parameters in a file called\
            .3dMSS.dbg.AFNI.args for debugging.
        if_name: Specify the column name that is designated for input files of\
            effect estimate. Default is 'InputFile'.
        show_allowed_options_flag: List of allowed options.
        sdiff_vars: Specify the factors for group comparisons.
        vt_formula: Specify varying smoothing terms. Two components are\
            required: the first one 'var' indicates the variable (e.g., subject)\
            around which the smoothing will vary while the second component\
            specifies the smoothing formulation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMssOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MSS_METADATA)
    params = v_3d_mss_params(
        prefix=prefix,
        jobs=jobs,
        mrr_formula=mrr_formula,
        lme_formula=lme_formula,
        random_effect=random_effect,
        qvars=qvars,
        mask=mask,
        bounds=bounds,
        prediction_table=prediction_table,
        data_table=data_table,
        cio_flag=cio_flag,
        rio_flag=rio_flag,
        help_flag=help_flag,
        dbg_args_flag=dbg_args_flag,
        if_name=if_name,
        show_allowed_options_flag=show_allowed_options_flag,
        sdiff_vars=sdiff_vars,
        vt_formula=vt_formula,
    )
    return v_3d_mss_execute(params, execution)


__all__ = [
    "V3dMssOutputs",
    "V3dMssParameters",
    "V_3D_MSS_METADATA",
    "v_3d_mss",
    "v_3d_mss_params",
]

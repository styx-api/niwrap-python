# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_REG_ANA_METADATA = Metadata(
    id="d0f5f9773868694c40c8514ea58aae0c0f7243a6.boutiques",
    name="3dRegAna",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dRegAnaParameters = typing.TypedDict('V3dRegAnaParameters', {
    "__STYXTYPE__": typing.Literal["3dRegAna"],
    "rows": float,
    "cols": float,
    "xydata": list[str],
    "model": str,
    "diskspace": bool,
    "workmem": typing.NotRequired[float | None],
    "rmsmin": typing.NotRequired[float | None],
    "fdisp": typing.NotRequired[float | None],
    "flof": typing.NotRequired[float | None],
    "fcoef": typing.NotRequired[list[str] | None],
    "rcoef": typing.NotRequired[list[str] | None],
    "tcoef": typing.NotRequired[list[str] | None],
    "bucket": typing.NotRequired[str | None],
    "brick": typing.NotRequired[list[str] | None],
    "datum": typing.NotRequired[str | None],
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
        "3dRegAna": v_3d_reg_ana_cargs,
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
        "3dRegAna": v_3d_reg_ana_outputs,
    }.get(t)


class V3dRegAnaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_reg_ana(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_fift: OutputPathType
    """Output fift dataset"""
    output_fith: OutputPathType
    """Output fith dataset"""
    output_fitt: OutputPathType
    """Output fitt dataset"""
    output_bucket: OutputPathType
    """Output bucket dataset"""
    output_bucket_brik: OutputPathType
    """Output bucket BRIK file"""


def v_3d_reg_ana_params(
    rows: float,
    cols: float,
    xydata: list[str],
    model: str,
    diskspace: bool = False,
    workmem: float | None = None,
    rmsmin: float | None = None,
    fdisp: float | None = None,
    flof: float | None = None,
    fcoef: list[str] | None = None,
    rcoef: list[str] | None = None,
    tcoef: list[str] | None = None,
    bucket: str | None = None,
    brick: list[str] | None = None,
    datum: str | None = None,
) -> V3dRegAnaParameters:
    """
    Build parameters.
    
    Args:
        rows: Number of input datasets.
        cols: Number of X variables.
        xydata: X variables and Y observations.
        model: Definition of linear regression model: reduced model (Y =\
            f(Xj1,...,Xjr)) and full model (Y = f(Xj1,...,Xjr,Xi1,...,Xiq)).
        diskspace: Print out disk space required for program execution.
        workmem: Number of megabytes of RAM to use for statistical workspace\
            (default = 750).
        rmsmin: Minimum rms error to reject constant model.
        fdisp: Display results for voxels whose F-statistic is > fval.
        flof: Minimum p value for F due to lack of fit.
        fcoef: Estimate of kth regression coefficient along with F-test for the\
            regression is written to AFNI `fift` dataset.
        rcoef: Estimate of kth regression coefficient along with coef. of mult.\
            deter. R^2 is written to AFNI `fith` dataset.
        tcoef: Estimate of kth regression coefficient along with t-test for the\
            coefficient is written to AFNI `fitt` dataset.
        bucket: Create one AFNI 'bucket' dataset having n sub-bricks; n=0\
            creates default output.
        brick: Specify the contents of the mth sub-brick in the bucket dataset.
        datum: Write the output in DATUM format. Choose from short (default) or\
            float.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dRegAna",
        "rows": rows,
        "cols": cols,
        "xydata": xydata,
        "model": model,
        "diskspace": diskspace,
    }
    if workmem is not None:
        params["workmem"] = workmem
    if rmsmin is not None:
        params["rmsmin"] = rmsmin
    if fdisp is not None:
        params["fdisp"] = fdisp
    if flof is not None:
        params["flof"] = flof
    if fcoef is not None:
        params["fcoef"] = fcoef
    if rcoef is not None:
        params["rcoef"] = rcoef
    if tcoef is not None:
        params["tcoef"] = tcoef
    if bucket is not None:
        params["bucket"] = bucket
    if brick is not None:
        params["brick"] = brick
    if datum is not None:
        params["datum"] = datum
    return params


def v_3d_reg_ana_cargs(
    params: V3dRegAnaParameters,
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
    cargs.append("3dRegAna")
    cargs.extend([
        "-rows",
        str(params.get("rows"))
    ])
    cargs.extend([
        "-cols",
        str(params.get("cols"))
    ])
    cargs.extend([
        "-xydata",
        *params.get("xydata")
    ])
    cargs.extend([
        "-model",
        params.get("model")
    ])
    if params.get("diskspace"):
        cargs.append("-diskspace")
    if params.get("workmem") is not None:
        cargs.extend([
            "-workmem",
            str(params.get("workmem"))
        ])
    if params.get("rmsmin") is not None:
        cargs.extend([
            "-rmsmin",
            str(params.get("rmsmin"))
        ])
    if params.get("fdisp") is not None:
        cargs.extend([
            "-fdisp",
            str(params.get("fdisp"))
        ])
    if params.get("flof") is not None:
        cargs.extend([
            "-flof",
            str(params.get("flof"))
        ])
    if params.get("fcoef") is not None:
        cargs.extend([
            "-fcoef",
            *params.get("fcoef")
        ])
    if params.get("rcoef") is not None:
        cargs.extend([
            "-rcoef",
            *params.get("rcoef")
        ])
    if params.get("tcoef") is not None:
        cargs.extend([
            "-tcoef",
            *params.get("tcoef")
        ])
    if params.get("bucket") is not None:
        cargs.extend([
            "-bucket",
            params.get("bucket")
        ])
    if params.get("brick") is not None:
        cargs.extend([
            "-brick",
            *params.get("brick")
        ])
    if params.get("datum") is not None:
        cargs.extend([
            "-datum",
            params.get("datum")
        ])
    return cargs


def v_3d_reg_ana_outputs(
    params: V3dRegAnaParameters,
    execution: Execution,
) -> V3dRegAnaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dRegAnaOutputs(
        root=execution.output_file("."),
        output_fift=execution.output_file("[PREFIX].fift+orig.HEAD"),
        output_fith=execution.output_file("[PREFIX].fith+orig.HEAD"),
        output_fitt=execution.output_file("[PREFIX].fitt+orig.HEAD"),
        output_bucket=execution.output_file("[PREFIX].bucket+orig.HEAD"),
        output_bucket_brik=execution.output_file("[PREFIX].bucket+orig.BRIK"),
    )
    return ret


def v_3d_reg_ana_execute(
    params: V3dRegAnaParameters,
    execution: Execution,
) -> V3dRegAnaOutputs:
    """
    Multiple linear regression analysis for AFNI datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dRegAnaOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_reg_ana_cargs(params, execution)
    ret = v_3d_reg_ana_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_reg_ana(
    rows: float,
    cols: float,
    xydata: list[str],
    model: str,
    diskspace: bool = False,
    workmem: float | None = None,
    rmsmin: float | None = None,
    fdisp: float | None = None,
    flof: float | None = None,
    fcoef: list[str] | None = None,
    rcoef: list[str] | None = None,
    tcoef: list[str] | None = None,
    bucket: str | None = None,
    brick: list[str] | None = None,
    datum: str | None = None,
    runner: Runner | None = None,
) -> V3dRegAnaOutputs:
    """
    Multiple linear regression analysis for AFNI datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        rows: Number of input datasets.
        cols: Number of X variables.
        xydata: X variables and Y observations.
        model: Definition of linear regression model: reduced model (Y =\
            f(Xj1,...,Xjr)) and full model (Y = f(Xj1,...,Xjr,Xi1,...,Xiq)).
        diskspace: Print out disk space required for program execution.
        workmem: Number of megabytes of RAM to use for statistical workspace\
            (default = 750).
        rmsmin: Minimum rms error to reject constant model.
        fdisp: Display results for voxels whose F-statistic is > fval.
        flof: Minimum p value for F due to lack of fit.
        fcoef: Estimate of kth regression coefficient along with F-test for the\
            regression is written to AFNI `fift` dataset.
        rcoef: Estimate of kth regression coefficient along with coef. of mult.\
            deter. R^2 is written to AFNI `fith` dataset.
        tcoef: Estimate of kth regression coefficient along with t-test for the\
            coefficient is written to AFNI `fitt` dataset.
        bucket: Create one AFNI 'bucket' dataset having n sub-bricks; n=0\
            creates default output.
        brick: Specify the contents of the mth sub-brick in the bucket dataset.
        datum: Write the output in DATUM format. Choose from short (default) or\
            float.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dRegAnaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_REG_ANA_METADATA)
    params = v_3d_reg_ana_params(
        rows=rows,
        cols=cols,
        xydata=xydata,
        model=model,
        diskspace=diskspace,
        workmem=workmem,
        rmsmin=rmsmin,
        fdisp=fdisp,
        flof=flof,
        fcoef=fcoef,
        rcoef=rcoef,
        tcoef=tcoef,
        bucket=bucket,
        brick=brick,
        datum=datum,
    )
    return v_3d_reg_ana_execute(params, execution)


__all__ = [
    "V3dRegAnaOutputs",
    "V3dRegAnaParameters",
    "V_3D_REG_ANA_METADATA",
    "v_3d_reg_ana",
    "v_3d_reg_ana_params",
]
